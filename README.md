# HOMEWORK EVOLUTION
 This is the homework requested by evolution team

 The Code is ready to run in the following list of devices:
 * Cisco IOS
 * Cisco NXoS
 * Cisco IOS xR
 * Fortigate
 * Huawei
 * Juniper

 Unfortunately, I was not able to emulate Aruba and Palo Alto devices.

 ## The program
 You can use the file update_netbox_sw_version.py to collect the version from devices and update the Netbox.

 If you want to clear the sw_version you can use the code clear_netbox_sw_version.py.
 CAUTION: This code will clear the device's sw_version custom_field.

 ## The env file
 All the sensitive data are inserted at the env file. So you must update it with the credentials of your network.

 For security reason, the env file will be ignored by the git.

 You will find a sample of the env file, you must update it with your data and rename it to env.

 ## Unit Test
 You can use the code test_model.py to run the Pytest.
