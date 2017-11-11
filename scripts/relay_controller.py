#!/usr/bin/env python
"""relay_controller.py
Usage:
    relay_controller.py --port=N (--on|--off) [--conf=file]
    relay_controller.py -h | --help

Options:
    -h --help    Show this help
    --port=N     Port number defined in the configuration file
    --on         Turn the relay ON
    --off        Turn the relay OFF
    --conf=FILE  Optional. Configuration file with relations between port
                 number and GPIO pinout [default: /etc/relay_controller.conf]
"""

from __future__ import print_function
import sys
import docopt
import ConfigParser
import syslog
import imp


# TODO: get rid of these dirthy debuging functions
# Print error to stderr
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    syslog.syslog(syslog.LOG_ERR, *args)


def dprint(*args):
    print(*args)
    syslog.syslog(*args)


try:
    imp.find_module('RPi.GPIO')
    import RPi.GPIO as GPIO
except RuntimeError:
    eprint('''Error importing RPi.GPIO!  This is probably because you need
        superuser privileges.  You can achieve this by using 'sudo' to run your
        script''')
except ImportError:
    import FakeRPi.GPIO as GPIO


def get_conf(conf):
    try:
        # TODO: use singleton to read config only once
        # Load configuration from file
        config = ConfigParser.ConfigParser()
        config.read(conf)
        dprint('Configuration file in {}'.format(conf))
        ports = config.items('Default')
    except ConfigParser.NoSectionError:
        # Could not load external configuration. Safe defaults
        dprint('Couldnt load external configuration file. Using safe defaults')
        # TODO: setup all possible pins for one RPi, not just 8
        ports = [  # Port: GPIO
            ('1', '18'),
            ('2', '19'),
            ('3', '20'),
            ('4', '21'),
            ('5', '22'),
            ('6', '23'),
            ('7', '24'),
            ('8', '25')
        ]
    return ports


def set_pin(port, action):
    # Setup board
    # TODO: Catch possible errors
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(int(port), GPIO.OUT)

    if action == 'on':
        mode = True
    else:
        mode = False

    dprint('Turning {} GPIO pin {}'.format(action, port))

    GPIO.output(int(port), mode)

    GPIO.cleanup()


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
