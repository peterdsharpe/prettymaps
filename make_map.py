import vsketch
from prettymaps import plot
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from layer_data import get_defaults
from pathlib import Path

this_dir = Path(__file__).parent


def make_map(
        location="Cambridge, MA",
        left_text="Cambridge, MA",
        top_text="42° 22' N, 71° 6' W",
        save_location=None,
        radius=2000,
        square=True,
        dilate=300,
        debug=False,
):
    # Init matplotlib figure
    fig, ax = plt.subplots(figsize=(18, 18), constrained_layout=True)

    layers, drawing_kwargs = get_defaults(
        square=square,
        dilate=dilate
    )

    if not debug:
        layers = plot(
            location, radius=radius,
            ax=ax,
            layers=layers,
            drawing_kwargs=drawing_kwargs
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
        xmin - 0.0225 * dx, ymin + 0.7 * dy,
        left_text,
        color='#2F3737',
        rotation=90,
        fontproperties=fm.FontProperties(fname=fontpath, size=50),
        va='center',
        ha='center',
    )
    # Draw top text
    ax.text(
        xmin + 0.7 * dx, ymax + 0.0225 * dy,
        top_text,
        color='#2F3737',
        fontproperties=fm.FontProperties(fname=fontpath, size=35),
        va='center',
        ha='center',
    )

    plt.savefig(save_location)
