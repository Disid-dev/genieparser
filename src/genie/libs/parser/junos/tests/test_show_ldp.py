# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ldp import (
    ShowLDPSession, ShowLDPInterface,
    ShowLDPInterfaceDetail)


# =================================
# Unit test for 'show ldp session'
# =================================
class TestShowLDPSession(unittest.TestCase):
    '''unit test for "show ldp session'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'ldp-session-information': {
            'ldp-session': [{
                'ldp-neighbor-address': '10.34.2.250',
                'ldp-session-state': 'Operational',
                'ldp-connection-state': 'Open',
                'ldp-remaining-time': '26',
                'ldp-session-adv-mode': 'DU'
            }]
        }
    }

    golden_output = {
        'execute.return_value':
        '''
          Address                           State       Connection  Hold time  Adv. Mode
        10.34.2.250                        Operational Open          26         DU
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

# ===============================================
# Unit test for 'show ldp interface {interface}'
# ===============================================
class TestShowLDPInterface(unittest.TestCase):
    '''unit test for "show ldp interface {interface}'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "ldp-interface-information": {
            "ldp-interface": {
                "interface-name": "ge-0/0/0.0",
                "ldp-interface-local-address": "10.169.14.157",
                "ldp-label-space-id": "10.169.14.240:0",
                "ldp-neighbor-count": "1",
                "ldp-next-hello": "3"
            }
        }
    }

    golden_output = {
        'execute.return_value':
        '''
            show ldp interface ge-0/0/0.0
            Interface          Address                          Label space ID   Nbr   Next
                                                                                count  hello
            ge-0/0/0.0         10.169.14.157                   10.169.14.240:0  1      3
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='ge-0/0/0.0')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPInterface(device=self.device)
        parsed_output = obj.parse(interface='ge-0/0/0.0')
        self.assertEqual(parsed_output, self.golden_parsed_output)

# =====================================================
# Unit test for 'show ldp interface {interface} detail'
# =====================================================
class TestShowLDPInterfaceDetail(unittest.TestCase):
    '''unit test for "show ldp interface {interface} detail'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "ldp-interface-information": {
            "ldp-interface": {
                "interface-name": "ge-0/0/0.0",
                "ldp-interface-local-address": "10.169.14.157",
                "ldp-label-space-id": "10.169.14.240:0",
                "ldp-neighbor-count": "1",
                "ldp-next-hello": "1",
                "ldp-transport-address": "10.169.14.240",
                "ldp-hello-interval": "5",
                "ldp-holdtime": "15",
            }
        }
    }

    golden_output = {
        'execute.return_value':
        '''
            show ldp interface ge-0/0/0.0 detail
            Interface          Address                          Label space ID   Nbr   Next
                                                                                count  hello
            ge-0/0/0.0         10.169.14.157                   10.169.14.240:0  1      1
            Hello interval: 5, Hold time: 15, Transport address: 10.169.14.240
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPInterfaceDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='ge-0/0/0.0')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPInterfaceDetail(device=self.device)
        parsed_output = obj.parse(interface='ge-0/0/0.0')
        self.assertEqual(parsed_output, self.golden_parsed_output)
if __name__ == '__main__':
    unittest.main()