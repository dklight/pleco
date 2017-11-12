#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import imp
import syslog
import sys


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
