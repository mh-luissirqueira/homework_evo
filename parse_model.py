"""
Used for parsing the output data from devices and return the software version
"""

# General Imports
import re

#### Local Methods called for the parser_data Method
def parser(data, pattern):
    """
    Parses the output from device using the pattern defined by model
    If not match is found, None is returned.
    """
    # Attempt to match the regex against the specific input
    match = re.search(pattern, data)
    if match:
        return match["version"]

    # No Match was found
    return None


#### Global Method Called for the get_sw_version program
def parse_data(data, device_type):
    """
    This method is called by the device_connection to parse the output of switch
    This Method calls the local method parser sending the pattern for Regular Expression
    based on the device model
    """
    if device_type == "cisco_ios":
        pattern = r'".+:(?P<version>\S+)"'

    elif device_type == "cisco_nxos":
        pattern = r"///(?P<version>\S+)"

    elif device_type == "juniper":
        pattern = r"Junos:\s+(?P<version>\S+)"

    elif device_type == "huawei":
        pattern = r"\d\s\((?P<version>\S+)\)"

    elif device_type == "fortinet":
        pattern = r"\s(?P<version>\S+),build"

    elif device_type == "cisco_xr":
        pattern = r"Version\s+(?P<version>\S+)\["

    return parser(data, pattern)
