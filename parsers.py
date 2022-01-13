# General Imports
import re

#### Local Methods called for the parser_data Method
def cisco_ios(data):
    data = re.search(r'"(.*?)"', data).group(0)
    data = data.replace('"', '')
    return data.split(':')[-1]

def cisco_nxos(data):
    return data.split('///')[-1]

def huawei(data):
    data = re.search(r'\((V.*?)\)', data).group(0)
    data = data.replace('(', '')
    return data.replace(')', '')

def fortinet(data):
    data = data.split('\n')
    data = data[0].split(' ')
    return data[2].split(',')[0]

#### Global Method Called for the get_sw_version program
def parse_data(data, device_type):
    if device_type == 'cisco_ios':
        return cisco_ios(data)
    
    elif device_type == 'cisco_nxos':
        return cisco_nxos(data)

    elif device_type == 'juniper':
        return data.replace('Junos: ', '')

    elif device_type == 'huawei':
        return huawei(data)
    
    elif device_type == 'fortinet':
        return fortinet(data)
    
    elif device_type == 'cisco_xr':
        return data

