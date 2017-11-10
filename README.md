# Pleco

[Pleco](https://github.com/dklight/pleco) is a complete fishtank controller,
intended to be run on a [RaspberryPI](https://www.raspberrypi.org/), with a
[relay board](https://en.wikipedia.org/wiki/Relay) connected. With that
hardware, it's posible to turn on and off any AC equipment (such as lights,
water pumps, etc).


# Features
 * Simple 220V on/of using relay controller board
 * Schedule on/of for lights, water pumps, etc


# Hardware
 * Raspberry PI, any model should be compatible
 * Relay board


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
 * FIXME


# TODO
 * Flask API to interact with relay_controller script
 * Simple Js GUI to interat with API
 * Electronic schematics
