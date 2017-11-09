#!/usr/bin/env python
"""relay_controller.py
Usage:
    relay_controller.py --port=N (--on|--off) [--conf=file]
    relay_controller.py -h | --help

Options:
    -h --help    Chow this help
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
import RPi.GPIO as GPIO


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

        port = arguments['--port']
        conf = arguments['--conf']
        if arguments['--on']:
            action = 'on'
        else:
            action = 'off'

        try:
            # Load configuration from file
            config = ConfigParser.ConfigParser()
            config.read(conf)
            ports = config.items('Default')
        except ConfigParser.NoSectionError:
            # Could not load external configuration. Safe defaults
            ports = {  # Port: GPIO
                '1': '18',
                '2': '19',
                '3': '20',
                '4': '21',
                '5': '22',
                '6': '23',
                '7': '24',
                '8': '25'
            }

        try:
            gpio_port = config.get('Default', port)
            # Execute action
            dprint('Configuration file in %d' % conf)

            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(int(gpio_port), GPIO.OUT)
            if action == 'on':
                mode = True
            else:
                mode = False

            dprint('''
                Turning {} port {} on GPIO gpio_port
                '''.format(action, port, gpio_port))

            GPIO.output(int(gpio_port), mode)

        except ConfigParser.NoOptionError:
            # Incorrect port
            eprint('Dont know how to reach port %d' % port)
            exit(129)
        except ConfigParser.NoSectionError:
            # Configuration file didn't exist
            try:
                gpio_port = ports[port]
                dprint('''
                    Turning {} port {} on GPIO gpio_port
                    '''.format(action, port, gpio_port))
            except KeyError:
                # Requested port not in defaults
                eprint('Dont know how to reach port ' + port)
                exit(129)

    # Handle invalid options
    except docopt.DocoptExit as e:
        eprint(e.message)
        exit(130)
