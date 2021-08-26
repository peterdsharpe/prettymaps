import os, sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from make_map import make_map

make_map(
    location="17 Pleasant Place, Cambridge, MA",
    left_text="Cambridge, MA",
    top_text="42° 22' N, 71° 6' W",
    save_location="cambridge.svg",
)