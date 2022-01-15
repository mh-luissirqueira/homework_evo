"""
Used to generate the command based on the device model
"""
#  General Imports
from jinja2 import Environment, FileSystemLoader

# Creating the Jinja2 Env
file_loader = FileSystemLoader(".")
env = Environment(loader=file_loader)


def get_version(driver):
    """
    Get the command based on the netmiko driver
    """
    template = env.get_template(f"/templates/{driver}_get_ver.j2")
    return template.render()
