def get_defaults(
        square=False,
        dilate=100,
):
    # Which OpenStreetMap layers to plot and their parameters:
    layers = {
        # Perimeter (in this case, a circle)
        'perimeter': {
            'circle': not square,
            'dilate': dilate,
        },
        # Streets and their widths
        'streets'  : {
            'width': {
                'motorway'    : 5,
                'trunk'       : 5,
                'primary'     : 4.5,
                'secondary'   : 4,
                'tertiary'    : 3.5,
                'residential' : 3,
                'service'     : 2,
                'unclassified': 2,
                'pedestrian'  : 2,
                'footway'     : 1,
                'track'       : 1,
                'bridleway'   : 1,
                'runway'      : 10,
                'taxiway'     : 5,
            },
        },
        'building' : {
            'tags'    : {
                'building': True,
                'landuse' : 'construction',
                'leisure' : 'track',
                'aeroway' : [
                    'terminal',
                    'hangar'
                ]
            }, 'union': False
        },
        'water'    : {
            'tags': {
                'natural' : ['water', 'bay', 'strait', 'spring', 'hot_spring'],
                'water'   : True,
                'place'   : 'sea',
                # 'waterway': True,
            }
        },
        'waterway': {
            # 'custom_filter': 'waterway'
            # 'tags' : {
            #     'waterway': True
            # },
            'width': {
                'canal' : 5,
                'dock'  : 10,
                'stream': 2,
            }
        },
        'green'    : {
            'tags': {
                'landuse': ['grass', 'orchard', 'meadow', 'cemetery', 'recreation_ground', 'village_green',
                            'allotments'],
                'natural': ['island', 'grassland'],
                'leisure': 'park'
            }
        },
        'scrub'    : {
            'tags': {
                'natural': 'scrub'
            }
        },
        'rocky'    : {
            'tags': {
                'natural': 'bare_rock'
            }
        },
        'walls'    : {
            'tags': {
                'historic': 'citywalls',
                'manmade' : 'embankment',
            }
        },
        'forest'   : {
            'tags': {
                'landuse': 'forest',
                'natural': 'wood',
                'tourism': 'camp_site',
            }
        },
        'garden'   : {
            'tags': {
                'leisure': ['garden', 'pitch', 'vineyard']
            }
        },
        'parking'  : {
            'tags': {
                'amenity' : 'parking',
                'highway' : 'pedestrian',
                'man_made': 'pier',
                'aeroway' : [
                    # 'aerodrome',
                    'apron',
                    'helipad',
                    'heliport',
                    'spaceport',
                ]
            }
        },
        'airways'  : {
            'tags': {
                'aeroway': [
                    'runway',
                    'taxiway',
                ]
            }
        },
        'beach'    : {
            'tags': {
                'natural': ['beach', 'heath'],
                'landuse': 'farmland',
            }
        },
        'wetlands' : {
            'tags': {
                'natural': ['wetland'],
                'leisure': ['nature_reserve'],
                'landuse': ['conservation'],
            }
        },
        'swamp'    : {
            'tags': {
                'wetland': ['swamp'],
            }
        },
        # 'railway'  : {
        #     'custom_filter': '["railway"~"rail|light_rail"]',
        #     # 'dilate'       : 2000
        # }
    }
    # drawing_kwargs:
    #   Reference a name previously defined in the 'layers' argument and specify matplotlib parameters to draw it
    drawing_kwargs = {
        # 'railway' : {
        #     'fc'    : '#2F3737',
        #     'ec'    : '#475657',
        #     'alpha' : 1,
        #     'lw'    : 0,
        #     'zorder': 3
        # },
        'background': {
            'fc'    : '#F2F4CB',
            'ec'    : '#dadbc1',
            'hatch' : 'ooo...',
            'zorder': -1},
        'perimeter' : {
            'fc'    : '#F2F4CB',
            'ec'    : '#dadbc1',
            'lw'    : 0,
            'hatch' : 'ooo...',
            'zorder': 0},
        'green'     : {
            'fc'    : '#D0F1BF',
            'ec'    : '#2F3737',
            'lw'    : 1,
            'zorder': 1
        },
        'scrub'     : {
            'fc'     : '#89d689',
            'ec'     : '#2F3737',
            'hatch_c': '#75bd75',
            'hatch'  : 'ooo...',
            'lw'     : 1,
            'zorder' : 1
        },
        'rocky'     : {
            'fc'     : '#a89e8a',
            'ec'     : '#2F3737',
            'hatch_c': '#a39c8f',
            'hatch'  : 'ooo...',
            'lw'     : 1,
            'zorder' : 1
        },
        'forest'    : {
            'fc'     : '#64B96A',
            'ec'     : '#2F3737',
            'hatch'  : 'ooo...',
            'hatch_c': '#5f8c62',
            'lw'     : 1,
            'zorder' : 1
        },
        'garden'    : {
            'fc'    : '#a9d1a9',
            'ec'    : '#8ab58a',
            'lw'    : 1,
            'zorder': 1
        },
        'water'     : {
            'fc'     : '#a1e3ff',
            'ec'     : '#2F3737',
            'hatch'  : 'ooo...',
            'hatch_c': '#85c9e6',
            'lw'     : 1,
            'zorder' : 2
        },
        'parking'   : {
            'fc'    : '#F2F4CB',
            'ec'    : '#2F3737',
            'lw'    : 1,
            'zorder': 3
        },
        'airways'   : {
            'fc'    : '#2F3737',
            'ec'    : '#2F3737',
            'lw'    : 2,
            'zorder': 3,
        },
        'streets'   : {
            'fc'    : '#2F3737',
            'ec'    : '#475657',
            'alpha' : 1,
            'lw'    : 0,
            'zorder': 3
        },
        'waterway' : {
            'fc'    : '#2f3737',
            'ec'    : '#a1e3ff',
            'alpha' : 1,
            'lw'    : 0,
            'zorder': 3
        },
        'walls'     : {
            'fc'    : '#2F3737',
            'ec'    : '#475657',
            'alpha' : 1,
            'lw'    : 0,
            'zorder': 3
        },
        'building'  : {
            'palette': ['#FFC857', '#E9724C', '#C5283D'],
            'ec'     : '#2F3737',
            'lw'     : .5,
            'zorder' : 4
        },
        'beach'     : {
            'fc'     : '#FCE19C',
            'ec'     : '#2F3737',
            'hatch_c': '#d4d196',
            'hatch'  : 'ooo...',
            'lw'     : 1,
            'zorder' : 3
        },
        'wetlands'  : {
            'fc'     : '#8ab964',
            'ec'     : '#2F3737',
            'hatch_c': '#738d5e',
            'hatch'  : 'ooo...',
            'lw'     : 1,
            'zorder' : 1,
        },
        'swamp'     : {
            'fc'     : '#738d5e',
            'ec'     : '#2F3737',
            'hatch_c': '#5a6e49',
            'hatch'  : 'ooo...',
            'lw'     : 1,
            'zorder' : 1,
        }
    }

    assert len(drawing_kwargs) == len(layers) + 1
    for k in layers.keys():
        assert k in drawing_kwargs.keys()

    if square:
        for k, v in layers.items():
            v['circle'] = False
            if 'dilate' not in v.keys():
                v['dilate'] = dilate

    return layers, drawing_kwargs
