"""
Program that connects to the network devices, collect the software version
and update the netbox sw_version custom_field
It will run only on devices that are as active at the Tenant NOC
"""
#  General Imports
import device_connection
import netbox_connection
import get_templates

print("Retrieving the Devices from Tenant NOC with Active status ...")
network_devices = netbox_connection.list_network_devices()

for network_device in network_devices:
    print()
    print(f"{network_device}: Starting the process ...")
    try:
        platform = netbox_connection.get_platform_driver(network_device.platform)

        print(f"{network_device}: Retrieving the command from template ...")
        commands = get_templates.get_version(platform.napalm_driver)

        print(f"{network_device}: Connecting to the Device ...")
        device_session = device_connection.ssh_connect(
            network_device.primary_ip4, platform.napalm_driver
        )

        version = device_connection.send_commands(device_session, commands)

        print(f"{network_device}: Disconnecting to the Device ...")
        device_connection.ssh_disconnect(device_session)

        if netbox_connection.device_sw_version_update(network_device, version):
            print(f"{network_device}: Done!!!")
        else:
            print(f"{network_device}: Error: Check the custom_field of the device ...")

    except Exception as e:
        print(f"{network_device}: Error: {e} ...")
