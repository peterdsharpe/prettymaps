import vsketch
import prettymaps
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from layer_data import get_defaults
from pathlib import Path
import time

this_dir = Path(__file__).parent


def make_map(
        figsize=(12, 12),
        location="Cambridge, MA",
        top_text="Cambridge, MA",
        left_text="42° 22' N, 71° 6' W",
        save_location=None,
        radius=1500,
        square=True,
        debug=False,
):
    t1 = time.perf_counter()

    layers_in, drawing_kwargs_in = get_defaults(
        square=square,
        dilate=radius * 0.2,
    )

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True, dpi=300)

    if not debug:
        layers = prettymaps.plot(
            query=location,
            ax=ax,
            radius=radius,
            layers=layers_in,
            drawing_kwargs=drawing_kwargs_in,
            osm_credit=False,
        )
        xmin, ymin, xmax, ymax = layers['perimeter'].bounds
    else:
        xmin, ymin, xmax, ymax = (0, 0, 1, 1)

    # Set bounds
    dx, dy = xmax - xmin, ymax - ymin
    ax.set_xlim(xmin - .05 * dx, xmax + .05 * dx)
    ax.set_ylim(ymin - .05 * dy, ymax + .05 * dy)

    # Draw left text
    fontpath = this_dir / "assets" / "PermanentMarker-Regular.ttf"
    fontpath = str(fontpath)

    ax.text(
        xmin - 0.0225 * dx, ymin + 0.6 * dy,
        left_text,
        color='#2F3737',
        rotation=90,
        fontproperties=fm.FontProperties(fname=fontpath, size=30),
        va='center',
        ha='center',
    )
    # Draw top text
    ax.text(
        xmin + 0.7 * dx, ymax + 0.0225 * dy,
        top_text,
        color='#2F3737',
        fontproperties=fm.FontProperties(fname=fontpath, size=30),
        va='center',
        ha='center',
    )

    t2 = time.perf_counter()
    print(f"{location} drawn in {t2 - t1:.3f} seconds.")

    return fig, ax


if __name__ == '__main__':
    make_map(save_location="test.png")
