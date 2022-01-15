"""
Script used for interaction with the network devices
It will handle the Connection, Commands, and Disconnection.
"""

# General Imports
import json
from netmiko import ConnectHandler
import parse_model

# Open the env file and retrieving the sensitive data
with open("env", encoding="utf-8") as env_file:
    env_data = json.load(env_file)

network_user = env_data["NETWORK_USER"]
network_pass = env_data["NETWORK_PASS"]


def ssh_connect(device_ip, device_type):
    """
    Connect to the device using the device_ip and driver
    The device_ip is a Netbox Class, So it must be converted and we must strip the mask
    """
    conn_data = {}
    conn_data["device_type"] = device_type
    conn_data["host"] = str(device_ip).split("/", maxsplit=1)[0]
    conn_data["username"] = network_user
    conn_data["password"] = network_pass
    return ConnectHandler(**conn_data)


def ssh_disconnect(device_connection):
    """
    Close the Network device connection
    """
    return device_connection.disconnect()


def send_commands(device_connection, command):
    """
    Send commands to the device and return the output using the parser to send only the version.
    """
    output = device_connection.send_command(command)
    return parse_model.parse_data(output, device_connection.device_type)
