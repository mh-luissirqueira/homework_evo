"""
Used to interact with Netbox
"""

#  General Imports
import json
import warnings
import pynetbox

# Disabling the warning since the Lab doesn't have SSL
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

# Open the env file and retrieving the sensitive data
with open("env", encoding="utf-8") as env_file:
    env_data = json.load(env_file)

netbox_domain = env_data["NETBOX_DOMAIN"]
netbox_token = env_data["NETBOX_TOKEN"]

# Creating the Netbox Env
netbox = pynetbox.api(netbox_domain, token=netbox_token)
netbox.http_session.verify = False


def list_network_devices():
    """
    Return all the devices from NOC Tenant with active state
    """
    return netbox.dcim.devices.filter(status="active", tenant="noc")


def get_platform_driver(platform):
    """
    Return the platform drive based on the device's platform name
    """
    return netbox.dcim.platforms.get(name=platform)


def device_sw_version_clean(device):
    """ "
    Clear the sw_version custom field of the device
    """
    device.custom_fields = {"sw_version": "None"}
    return device.save()


def device_sw_version_update(device, version):
    """
    Update the sw_version custom field of the device
    """
    if device.custom_fields["sw_version"] != version:
        device.custom_fields = {"sw_version": version}
        return device.save()
    return True
