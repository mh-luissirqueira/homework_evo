"""
O que este Script vai fazer???
"""

#  Modules Imports
import pynetbox, json
import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# Abrindo o Arquivo com as Credenciais
with open('env') as env_file:
    env_data = json.load(env_file)

# Coletando as credenciais e variaveis necessárias
network_user = env_data['NETWORK_USER']
network_pass = env_data['NETWORK_PASS']
netbox_domain = env_data['NETBOX_DOMAIN']
netbox_token = env_data['NETBOX_TOKEN']

# Criando o env do Netbox
netbox = pynetbox.api(netbox_domain, token=netbox_token)
netbox.http_session.verify = False

print('Listando todos os Network Devices ...')
devices = netbox.dcim.devices.filter(status='active',tenant='noc')

for device in devices:
    print()
    print(f'{device}: Iniciando processamento ...')
    try:
        device.custom_fields = {'sw_version': 'None'}
        device.save()
        print(f'{device}: Feito!!!')
    except Exception as e:
        print(f'{device}: Erro: {e} ...')
