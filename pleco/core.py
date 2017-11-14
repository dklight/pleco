# -*- coding: utf-8 -*-
"""
Pleco: core module

The Pleco core module intends to provided all the general, common
functionality.

Todo:
    * Get rid of debuging funnctions
"""

from __future__ import print_function
import sys
import syslog
import ConfigParser
import os


# TODO: get rid of these dirthy debuging functions
# Print error to stderr
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    syslog.syslog(syslog.LOG_ERR, *args)


def dprint(*args):
    print(*args)
    syslog.syslog(*args)


def get_default_conf():
    """
    Set safe (hardcoded) configuration settings

    Set safe configuration settings for the case when no configuration file
    was found.

    Returns:
        list(str, str): list of (port, gpio_port) configuration settings

    Todo:
        * Setup all possible pins for one RPi, not just 8
    """

    dprint('Couldn\'t load external configuration file. Using safe defaults')
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


def get_conf(conf_file):
    """
    Load the configuration from file or asume safe defaults.

    Load the configuration from file. If no value is provided, this function
    will look for a file called pleco.conf in the same directory where the
    programm is running. If that file isn't present either, it will look for a
    global configuration file in /etc/pleco.conf. If that file isnt present,
    the function will call get_default_conf() to get safe defaults.

    Arguments:
        conf_file (str): absolute unix path to the configuration file
            (pleco.conf)

    Returns:
        list(str, str): list of (port, gpio_port) configuration settings

    Todo:
        * Use singleton to read config only once
    """

    config = ConfigParser.ConfigParser()

    if not conf_file:  # Configuration file not provided
        FILE = 'pleco.conf'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        local_file = '{}/{}'.format(dir_path, FILE)
        if os.path.isfile(local_file):  # Search for local file
            # Local file exist
            dprint('Trying local conf file {}'.format(local_file))
            conf_file = local_file
        else:  # use global default file
            global_file = '/etc/{}'.format(FILE)
            dprint('Trying global conf file {}'.format(local_file))
            conf_file = global_file
    else:  # Configuration file provided
        dprint('Trying provided file {}'.format(conf_file))
        if not os.path.isfile(conf_file):  # Provided file don't exist
            conf_file = None

    try:
        if conf_file:
            config.read(conf_file)
            dprint('Configuration file in {}'.format(conf_file))
            ports = config.items('Default')
        else:
            ports = get_default_conf()
    except ConfigParser.NoSectionError:
        # Could not load external configuration. Safe defaults
        ports = get_default_conf()

    return ports
