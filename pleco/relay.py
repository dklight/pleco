# -*- coding: utf-8 -*-
"""
Pleco: relay module

The Pleco relay module intends to provided all functionality around relay
boards, the one's that let turn's appliances on or off.

If this module is not run on a real Raspberry Pi, it relies on a fake
implementation. That's useful for testing purposes.
"""

import imp
import logging

logger = logging.getLogger(__name__)

try:
    imp.find_module('RPi.GPIO')
    import RPi.GPIO as GPIO
except RuntimeError:
    logger.error('''Error importing RPi.GPIO!  This is probably because you need
        superuser privileges.  You can achieve this by using 'sudo' to run your
        script''')
except ImportError:
    import FakeRPi.GPIO as GPIO


def set_pin(port, action):
    """
    Set a Raspberry Pi GPIO pin on or off.

    Set a Raspberry Pi GPIO pin on or off.

    Arguments:
        port (int): the GPIO.BOARD pin of the Raspberry Pi
        action (str): the state that should be written on the port (on|off)

    Todo:
        * return some usefull status
        * Catch possible exceptions
    """

    # Setup board
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(int(port), GPIO.OUT)

    if action == 'on':
        mode = True
    else:
        mode = False

    logger.info('Turning {} GPIO pin {}'.format(action, port))

    GPIO.output(int(port), mode)

    GPIO.cleanup()
