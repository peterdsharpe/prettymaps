# Pretty Maps

Tools to make pretty maps of areas of interest.

## Usage

Assuming you have Python installed:

1. Install dependencies: `pip install -r requirements.txt`
2. Run `make_map.py` directly (`python make_map.py`), or import it into your own script. (See the `__main__` block in `make_map.py` for example usage.)
3. Wait. It might take a few minutes (up to 10-ish) to download, cache, and draw all of the data for the region requested.

### Platform

Only tested on Python 3.9 installed via Anaconda distribution on Ubuntu 20.04 via Windows Subsystem for Linux. YMMV. In particular, I have issues running on Windows due to an unhandled exception in the `osmnx` package. It
can probably run in [Google Colab](https://colab.research.google.com/?utm_source=scs-index) if you're having issues.

### Example
![Example Map](example-cambridge.jpeg)

## Attribution

* [@marceloprates](https://github.com/marceloprates/prettymaps)
* [OpenStreetMap](https://www.openstreetmap.org/#map=5/38.007/-95.844)
* [osmnx](https://github.com/gboeing/osmnx)
* [matplotlib](https://matplotlib.org/)
* [shapely](https://shapely.readthedocs.io/en/stable/index.html)
* [vsketch](https://github.com/abey79/vsketch)
  libraries.
