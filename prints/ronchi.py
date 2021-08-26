import os, sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from make_map import make_map

make_map(
    location="45.82515597733224, 13.502543539075095",
    left_text="Ronchi dei Legionari, FVG, Italia",
    top_text="45° 50' N, 13° 30' E",
    save_location="ronchi.svg",
)