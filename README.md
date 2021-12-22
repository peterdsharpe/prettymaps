# Pretty Maps

Tools to make pretty maps of areas of interest, with my own tweaks.

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Run `make_map.py` directly, or import it into your own script. (See the `__main__` block for example usage.)

### Platform

Only tested on Python 3.9 installed via Anaconda distribution on Ubuntu 20.04 via Windows Subsystem for Linux. YMMV. It
can probably run in Google Colab if you're having issues.

## Attribution

Based on:

* [marceloprates/prettymaps](https://github.com/marceloprates/prettymaps) (Forked from here)
* [OpenStreetMap](https://www.openstreetmap.org/#map=5/38.007/-95.844)
* [osmnx](https://github.com/gboeing/osmnx), [matplotlib](https://matplotlib.org/)
  , [shapely](https://shapely.readthedocs.io/en/stable/index.html) and [vsketch](https://github.com/abey79/vsketch)
  libraries.

Example:
![Example Map](example-cambridge.jpeg)