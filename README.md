# Pleco

[Pleco](https://github.com/dklight/pleco) is a complete fishtank controller,
intended to be run on a [RaspberryPI](https://www.raspberrypi.org/), with a
[relay board](https://en.wikipedia.org/wiki/Relay) connected. With that
hardware, it's posible to turn on and off any AC equipment (such as lights,
water pumps, etc).


# Features
 * Simple appliances (100V-220V) on/off using relay controller board
 * Schedule on/off for lights, water pumps, etc


# Hardware
 * Raspberry PI (any model should be compatible)
 * Relay board

# Usage
## CLI
For now, pleco is just a CLI script for turning on and off electrical (AC)
stuff.

Each electrical appliance should be conected to a port in the relay board. Each
port should be asociated to a Raspberry PI GPIO pin.

To turn a port on use the relay_controller.py script as follows:

```bash
./relay_controller.py --port=1 --on
```

To turn a port off simply use the relay_controller.py script as follows:

```bash
./relay_controller.py --port=1 --off
```

## Scheduling actions
It is possible to use [Cron](https://es.m.wikipedia.org/wiki/Cron_(Unix))
to schedule on/off actions:

```bash
root@raspecera:/etc/cron.d# cat light_controller
# Main Lights
0 08 * * * root /usr/bin/python /usr/local/bin/relay_contro
ler.py --port=4 --on --conf=/etc/relay_controller.conf
0 20 * * * root /usr/bin/python /usr/local/bin/relay_contro
ler.py --port=4 --off --conf=/etc/relay_controller.conf
```

For additional help with Cron syntax use [crontab.guru](https://crontab.guru)

# License
GNU General Public License v3.0

See [COPYING](COPYING) to see the full text.


# Install
To install, SSH into your Raspberry PI, and run:

```bash
git clone https://github.com/dklight/pleco.git
cd pleco
pip install -r requirements.txt
```

# Changelog
## 2017-11-09
 * Initial commit
 * Add basic doc
 * License GPLv3


# TODO
 * Isolate relay functions into library
 * Flask API to interact with the relay module
 * Simple Js GUI to interat with API
 * Testing!
 * CI with TravisCI
 * Electronic schematics
