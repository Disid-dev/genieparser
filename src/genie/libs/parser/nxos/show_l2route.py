"""show_l2route.py

NXOS parsers for the following show commands:
    * show l2route evpn mac all
    * show l2route evpn mac evi <WORD> mac <WORD>

"""

import re


from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# ====================================================
#  schema for 'show l2route evpn mac all'
# ====================================================
class ShowL2routeEvpnMacSchema(MetaParser):
    """Schema for show l2route evpn mac all"""

    schema = {
        'topology':
            {Any():
                {'mac_address':
                    {Any():
                        {'prod': str,
                         'flags': str,
                         'seq_no': str,
                         'next_hops': str}
                    },
                }
            },
        }

# ====================================================
#  parser for 'show l2route evpn mac all'
# ====================================================
class ShowL2routeEvpnMac(ShowL2routeEvpnMacSchema):
    """Parser for show l2route evpn mac all"""

    cli_command = 'show l2route evpn mac all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 100         fa16.3e59.d0b2 BGP    SplRcv        0          10.166.1.1
            p1 = re.compile(r'^\s*(?P<topology>[0-9]+) +(?P<mac_address>[a-z0-9\.]+) '
                '+(?P<prod>[a-zA-Z]+) +(?P<flags>[a-zA-Z\,]+) +(?P<seq_no>[0-9]+) '
                '+(?P<next_hops>[a-zA-Z0-9\/\.]+)$')
            m = p1.match(line)
            if m:

                topology = str(m.groupdict()['topology'])
                mac_address = str(m.groupdict()['mac_address'])

                if 'topology' not in ret_dict:
                    ret_dict['topology'] = {}
                if topology not in ret_dict['topology']:
                    ret_dict['topology'][topology] = {}
                if 'mac_address' not in ret_dict['topology'][topology]:
                    ret_dict['topology'][topology]['mac_address'] = {}
                if mac_address not in ret_dict['topology'][topology]['mac_address']:
                    ret_dict['topology'][topology]['mac_address'][mac_address] = {}

                ret_dict['topology'][topology]['mac_address'][mac_address]['prod'] = \
                    str(m.groupdict()['prod'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['flags'] = \
                    str(m.groupdict()['flags'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['seq_no'] = \
                    str(m.groupdict()['seq_no'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['next_hops'] = \
                    str(m.groupdict()['next_hops'])

                continue

        return ret_dict

# =========================================================
#  schema for 'show l2route evpn mac evi <WORD> mac <WORD>'
# =========================================================
class ShowL2routeEvpnMacEviSchema(MetaParser):
    """Schema for show l2route evpn mac evi <WORD> mac <WORD>"""

    schema = {
        'topology':
            {Any():
                {'mac_address':
                    {Any():
                        {'prod': str,
                         'flags': str,
                         'seq_no': str,
                         'next_hops': str}
                    },
                }
            },
        }

# =========================================================
#  parser for 'show l2route evpn mac evi <WORD> mac <WORD>'
# =========================================================
class ShowL2routeEvpnMacEvi(ShowL2routeEvpnMacEviSchema):
    """Parser for show l2route evpn mac evi <WORD> mac <WORD>"""

    cli_command = 'show l2route evpn mac evi {evi} mac {mac}'

    def cli(self, evi, mac, output=None):
        cmd = ""
        if evi and mac:
            cmd = self.cli_command.format(evi=evi, mac=mac)

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # 100         fa16.3e59.d0b2 BGP    SplRcv        0          10.166.1.1
        p1 = re.compile(r'^\s*(?P<topology>[0-9]+) +(?P<mac_address>[a-z0-9\.]+) '
            '+(?P<prod>[a-zA-Z]+) +(?P<flags>[a-zA-Z\,]+) +(?P<seq_no>[0-9]+) '
            '+(?P<next_hops>[a-zA-Z0-9\/\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:

                topology = str(m.groupdict()['topology'])
                mac_address = str(m.groupdict()['mac_address'])

                if 'topology' not in ret_dict:
                    ret_dict['topology'] = {}
                if topology not in ret_dict['topology']:
                    ret_dict['topology'][topology] = {}
                if 'mac_address' not in ret_dict['topology'][topology]:
                    ret_dict['topology'][topology]['mac_address'] = {}
                if mac_address not in ret_dict['topology'][topology]['mac_address']:
                    ret_dict['topology'][topology]['mac_address'][mac_address] = {}

                ret_dict['topology'][topology]['mac_address'][mac_address]['prod'] = \
                    str(m.groupdict()['prod'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['flags'] = \
                    str(m.groupdict()['flags'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['seq_no'] = \
                    str(m.groupdict()['seq_no'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['next_hops'] = \
                    str(m.groupdict()['next_hops'])

                continue

        return ret_dict

# vim: ft=python ts=8 sw=4 et

# ====================================================
#  schema for 'show l2route evpn mac-ip evi <evi>'
# ====================================================
class ShowL2routeEvpnMacIpEviSchema(MetaParser):
    """Schema for show l2route evpn mac-ip evi <evi>"""

    schema = {
        'topology':
            {Any():
                {'mac_address':
                    {Any():
                        {'prod': str,
                         'flags': str,
                         'seq_no': str,
                         'host_ip': str,
                         'next_hops': str}
                    },
                }
            },
        }

# ====================================================
#  parser for 'show l2route evpn mac-ip evi <evi>'
# ====================================================
class ShowL2routeEvpnMacIpEvi(ShowL2routeEvpnMacIpEviSchema):
    """Parser for show l2route evpn mac-ip evi <evi>"""

    cli_command = 'show l2route evpn mac-ip evi {evi}'

    def cli(self, evi, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(evi=evi))
        else:
            out = output

        ret_dict = {}
        # 101         fa16.3e04.e54a BGP    --            0          100.101.8.3    66.66.66.66
        # 101         fa16.3ec5.fcab HMM    --            0          100.101.1.4    Local
        p1 = re.compile(r'^\s*(?P<topology>[0-9]+) +(?P<mac_address>'
            '[a-z0-9\.]+) +(?P<prod>[a-zA-Z]+) +(?P<flags>[a-zA-Z\,\-]+)'
            ' +(?P<seq_no>[0-9]+) +(?P<host_ip>[\d\.]+) +(?P<next_hops>'
            '[a-zA-Z0-9\/\.]+)')            

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                topology = ret_dict.setdefault('topology', {}).\
                    setdefault(group['topology'], {}). \
                    setdefault('mac_address', {}).\
                    setdefault(group['mac_address'], {})
                topology.update({'prod' : group['prod']})
                topology.update({'flags' : group['flags']})
                topology.update({'seq_no' : group['seq_no']})
                topology.update({'host_ip' : group['host_ip']})
                topology.update({'next_hops' : group['next_hops']})
                continue

        return ret_dict