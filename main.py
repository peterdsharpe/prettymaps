import vsketch
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from defaults import get_defaults

# Init matplotlib figure
fig, ax = plt.subplots(figsize=(18, 18), constrained_layout=True)

layers, drawing_kwargs = get_defaults(
    square=True,
    dilate=300
)

layers = plot(
    # Address:
    # '45.82506,13.50276', radius=2000, # Ronchi town center
    # 'Monfalcone, Italy', radius=2000,
    '17 Pleasant Place, Cambridge, MA', radius=2000,
    ax=ax,
    layers=layers,
    drawing_kwargs=drawing_kwargs
)

# Set bounds
xmin, ymin, xmax, ymax = layers['perimeter'].bounds
dx, dy = xmax-xmin, ymax-ymin
ax.set_xlim(xmin-.06*dx, xmax+.06*dx)
ax.set_ylim(ymin-.06*dy, ymax+.06*dy)

# Draw left text
ax.text(
    xmin-.06*dx, ymin+.5*dy,
    'SS Luna: Cambridge, MA',
    color = '#2F3737',
    rotation = 90,
    fontproperties = fm.FontProperties(fname = r'assets/PermanentMarker-Regular.ttf', size = 35),
    )
# Draw top text
ax.text(
    xmax-.35*dx, ymax+.02*dy,
    "42° 22' N, 71° 6' W",
    color = '#2F3737',
    fontproperties = fm.FontProperties(fname = r'assets/PermanentMarker-Regular.ttf', size = 20),
    )

# plt.savefig("prints/ronchi.svg")
# plt.savefig("prints/monfalcone.svg")
plt.savefig("prints/cambridge.svg")
