#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""pleco_cli.py
Usage:
    pleco_cli.py --port=N (--on|--off) [--conf=file]
    pleco_cli.py -h | --help

Options:
    -h --help    Show this help
    --port=N     Port number defined in the configuration file
    --on         Turn the relay ON
    --off        Turn the relay OFF
    --conf=FILE  Optional. Configuration file with relations between port
                 number and GPIO pinout [default: /etc/pleco.conf]
"""

from __future__ import print_function
import docopt
import sys
import syslog
from relay import set_pin
from core import get_conf


# TODO: get rid of these dirthy debuging functions
# Print error to stderr
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    syslog.syslog(syslog.LOG_ERR, *args)


def dprint(*args):
    print(*args)
    syslog.syslog(*args)


if __name__ == '__main__':

    try:
        # Parse arguments, use file docstring as a parameter definition
        arguments = docopt.docopt(__doc__)

        port_alias = arguments['--port']
        conf = arguments['--conf']
        if arguments['--on']:
            action = 'on'
        else:
            action = 'off'

        # TODO: default must be completed by docopt, but anyway, if not passed,
        # set default conf file

        # Converto to dict instead of list of tuples for easy of use
        ports = dict(get_conf(conf))

        if port_alias in ports.keys():
            # TODO: check if the configured pin is valid
            set_pin(ports[port_alias], action)
        else:
            # Incorrect port
            eprint('Incorrect port {}'.format(port_alias))
            exit(129)

    # Handle invalid options
    except docopt.DocoptExit as e:
        eprint(e.message)
        exit(130)
