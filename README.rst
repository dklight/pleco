Pleco
=====

|License: GPL v3|

`Pleco`_ is a complete fishtank controller, intended to be run on a
`RaspberryPI`_, with a `relay board`_ connected. With that hardware,
it’s possible to turn on and off any AC equipment (such as lights, water
pumps, etc).

Features
========

-  Simple appliances (100V-220V) on/off using relay controller board
-  Schedule on/off for lights, water pumps, etc

Hardware
========

-  Raspberry PI (any model should be compatible)
-  Relay board

Install
=======

To install, SSH into your Raspberry PI, and run:

.. code:: bash

    git clone https://github.com/dklight/pleco.git
    cd pleco
    pip install -r requirements.txt

Usage
=====

CLI
---

For now, pleco is just a CLI script for turning on and off electrical
(AC) stuff.

Each electrical appliance should be conected to a port in the relay
board. Each port should be asociated to a Raspberry PI GPIO pin.

To turn a port on use the pleco_cli.py script as follows:

.. code:: bash

    ./pleco_cli.py --port=1 --on

To turn a port off simply use the pleco_cli.py script as follows:

.. code:: bash

    ./pleco_cli.py --port=1 --off

Scheduling actions
------------------

It is possible to use `Cron`_ to schedule on/off actions:

.. code:: bash

    root@raspecera:/etc/cron.d# cat light_controller
    # Main Lights
    0 08 * * * root /usr/bin/python /usr/local/bin/pleco_cli.py --port=4 --on 
        --conf=/etc/pleco.conf
    0 20 * * * root /usr/bin/python /usr/local/bin/pleco_cli.py --port=4 --off 
        --conf=/etc/pleco.conf

For additional help with Cron syntax use `crontab.guru`_

License
=======

GNU General Public License v3.0

See `LICENSE`_ to see the full text.

Changelog
=========

2017-11-09
----------

-  Initial commit
-  Add basic doc
-  License GPLv3

.. section-1:

2017-11-11
----------

-  Complete repository reorganization
-  Split code into modules

TODO
====

-  Flask API to interact with the relay module
-  Simple Js GUI to interat with API
-  Testing!
-  CI with TravisCI
-  Electronic schematics

.. _Pleco: https://github.com/dklight/pleco
.. _RaspberryPI: https://www.raspberrypi.org/
.. _relay board: https://en.wikipedia.org/wiki/Relay
.. _Cron: https://es.m.wikipedia.org/wiki/Cron_(Unix)
.. _crontab.guru: https://crontab.guru
.. _LICENSE: LICENSE

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
