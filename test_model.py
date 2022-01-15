"""
We will use the Pytest's function called assert. As Pytest is a binary I don't need to import it
"""
#  General Imports
from parse_model import parse_data


def test_cisco_ios():
    """
    Unit Test for Cisco IOS
    """
    ## Testing the positive case
    model_output_list = [
        'System image file is "flash:c3750-advipservicesk9-mz.122-46.SE.bin"',
        'System image file is "flash:c3750-advipservicesk9-mz.122-46.SE.bin',
        'System image file is "bootflash:cat4500-ipbasek9-mz.122-31.SGA9.bin"',
    ]

    model_answer_list = [
        "c3750-advipservicesk9-mz.122-46.SE.bin",
        None,
        "cat4500-ipbasek9-mz.122-31.SGA9.bin",
    ]

    for model_output, model_answer in zip(model_output_list, model_answer_list):
        print(model_output)

        # Perform parsing, print structured data, and validate
        parser_output = parse_data(model_output, "cisco_ios")
        print(parser_output)
        assert parser_output == model_answer


def test_cisco_nxos():
    """
    Unit Test for Cisco Nexus
    """
    ## Testing the positive case
    model_output_list = [
        "NXOS image file is: bootflash:///nxos.7.0.3.I7.9.bin",
        "NXOS image file is: bootflash:nxos.7.0.3.I7.9.bin",
    ]

    model_answer_list = ["nxos.7.0.3.I7.9.bin", None]

    for model_output, model_answer in zip(model_output_list, model_answer_list):
        print(model_output)

        # Perform parsing, print structured data, and validate
        parser_output = parse_data(model_output, "cisco_nxos")
        print(parser_output)
        assert parser_output == model_answer


def test_cisco_xr():
    """
    Unit Test for Cisco IOS xR
    """
    ## Testing the positive case
    model_output_list = [
        "Cisco IOS XR Software, Version 6.1.2[Default]",
        "Cisco IOS XR Software, Version 6.1.2 [Default]",
    ]

    model_answer_list = ["6.1.2", None]

    for model_output, model_answer in zip(model_output_list, model_answer_list):
        print(model_output)

        # Perform parsing, print structured data, and validate
        parser_output = parse_data(model_output, "cisco_xr")
        print(parser_output)
        assert parser_output == model_answer


def test_huawei():
    """
    Unit Test for Huawei
    """
    ## Testing the positive case
    model_output_list = [
        "Software      Version   : VRP (R) Software, Version 5.170 (V200R010C00SPC600)",
        "Software      Version   : VRP (R) Software, Version 5.170 (V200R010C00SPC600",
    ]

    model_answer_list = ["V200R010C00SPC600", None]

    for model_output, model_answer in zip(model_output_list, model_answer_list):
        print(model_output)

        # Perform parsing, print structured data, and validate
        parser_output = parse_data(model_output, "huawei")
        print(parser_output)
        assert parser_output == model_answer


def test_juniper():
    """
    Unit Test for Juniper
    """
    ## Testing the positive case
    model_output_list = ["Junos: 18.2R3-S3.11", "Junos:18.2R3-S3.11"]

    model_answer_list = ["18.2R3-S3.11", None]

    for model_output, model_answer in zip(model_output_list, model_answer_list):
        print(model_output)

        # Perform parsing, print structured data, and validate
        parser_output = parse_data(model_output, "juniper")
        print(parser_output)
        assert parser_output == model_answer


def test_fortinet():
    """
    Unit Test for Fortinet
    """
    ## Testing the positive case
    model_output_list = [
        """Version: FortiGate-1500D v6.0.9,build0335,200121 (GA)
           Virus-DB: 74.01987(2020-02-02 22:32)
           Extended DB: 1.00000(2018-04-09 18:07)
           Extreme DB: 1.00000(2018-04-09 18:07)
           IPS-DB: 6.00741(2015-12-01 02:30)
           IPS-ETDB: 6.00741(2015-12-01 02:30)
           APP-DB: 6.00741(2015-12-01 02:30)
           INDUSTRIAL-DB: 6.00741(2015-12-01 02:30)
           Serial-Number: FG1K5D3I17803571
           IPS Malicious URL Database: 3.00055(2021-06-29 06:39)
           Botnet DB: 4.00700(2021-06-30 18:06)
           BIOS version: 05000006
           System Part-Number: P12917-09
           Log hard disk: Available
           Hostname: FW02-MH1
           Operation Mode: NAT
           Current virtual domain: root
           Max number of virtual domains: 10
           Virtual domains status: 4 in NAT mode, 6 in TP mode
           Virtual domain configuration: enable
           FIPS-CC mode: disable
           Current HA mode: standalone
           Branch point: 0335
           Release Version Information: GA
           FortiOS x86-64: Yes
           System time: Fri Jan 14 20:49:02 2022""",
        "Version: FortiGate-1500D v6.0.9,build0335,200121 (GA)",
        "Version: FortiGate-1500D v6.0.9 ,build0335,200121 (GA)",
    ]

    model_answer_list = ["v6.0.9", "v6.0.9", None]

    for model_output, model_answer in zip(model_output_list, model_answer_list):
        print(model_output)

        # Perform parsing, print structured data, and validate
        parser_output = parse_data(model_output, "fortinet")
        print(parser_output)
        assert parser_output == model_answer
