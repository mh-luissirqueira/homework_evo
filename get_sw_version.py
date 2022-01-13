"""
"""

#  General Imports
import pynetbox, json
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import warnings
from parsers import parse_data

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# Open the env file and retrieving the sensitive data
with open('env') as env_file:
    env_data = json.load(env_file)

network_user = env_data['NETWORK_USER']
network_pass = env_data['NETWORK_PASS']
netbox_domain = env_data['NETBOX_DOMAIN']
netbox_token = env_data['NETBOX_TOKEN']

# Creating the Netbox Env
netbox = pynetbox.api(netbox_domain, token=netbox_token)
netbox.http_session.verify = False

# Creating the Jinja2 Env
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

print('Retrieving the Devices from Tenant NOC with Active status ...')
devices = netbox.dcim.devices.filter(status='active',tenant='noc')

for device in devices:
    print()
    print(f'{device}: Starting the process ...')
    try:
        platform = netbox.dcim.platforms.get(name=device.platform)
        print(f'{device}: Retrieving the command from template ...')
        template = env.get_template(f"/templates/{platform.napalm_driver}_get_ver.j2")
        comandos =  template.render()
        conn_data = {}
        conn_data["device_type"] = platform.napalm_driver
        address = str(device.primary_ip4).replace('/32','')
        conn_data["host"] = address.split('/')[0]
        conn_data["username"] = network_user
        conn_data["password"] = network_pass
        if conn_data["device_type"] == 'fortinet':
            conn_data["username"] = 'maxihost'
            conn_data["password"] = '@ddwcz8bJ'
        print(f'{device}: Connecting to the Device ...')
        with ConnectHandler(**conn_data) as net_connect:
            output = ''
            output = net_connect.send_command(comandos)
        version = parse_data(output, conn_data["device_type"])
        device.custom_fields = {'sw_version': version}
        device.save()        
        print(device,":", version)
        print(f'{device}: Done!!!')
    except Exception as e:
        print(f'{device}: Error: {e} ...')
