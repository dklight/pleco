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
                 number and GPIO pinout [default: pleco.conf]
"""

import docopt
from relay import set_pin
from core import get_conf
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        # Parse arguments, use file docstring as a parameter definition
        logger.debug('Parsing arguments')
        arguments = docopt.docopt(__doc__)

        port_alias = arguments['--port']
        conf = arguments['--conf']
        if arguments['--on']:
            action = 'on'
        else:
            action = 'off'

        logger.debug('Detected action: {}'.format(action))

        # Converto to dict instead of list of tuples for easy of use
        ports = dict(get_conf(conf))

        if port_alias in ports.keys():
            # TODO: check if the configured pin is valid
            set_pin(ports[port_alias], action)
        else:
            # Incorrect port
            logger.error('Incorrect port {}'.format(port_alias))
            exit(129)

    # Handle invalid options
    except docopt.DocoptExit as e:
        logger.error(e.message, exc_info=True)
        exit(130)
