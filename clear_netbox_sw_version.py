"""
Script to Clear all the sw_version custom_field from devices of the NOC Tenant and Active state.
CAUTION: Take care to use it on production env, since It'll clear data from active devices.
"""
#  Modules Imports
import netbox_connection

print("Retrieving the Devices from Tenant NOC with Active status ...")
network_devices = netbox_connection.list_network_devices()

for network_device in network_devices:
    print()
    print(f"{network_device}: Starting the process ...")
    try:
        netbox_connection.device_sw_version_clean(network_device)
        print(f"{network_device}: Done!!!")
    except Exception as e:
        print(f"{network_device}: Error: {e} ...")
