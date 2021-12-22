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
                'waterway': True,
            }
        },
        # 'morewater' : {
        #     # 'custom_filter': 'waterway'
        #     'tags': {
        #         'waterway': True
        #     },
        #     # 'width': {
        #     #     'canal': 5,
        #     #     'dock': 10,
        #     # }
        # },
        'green'    : {
            'tags': {
                'landuse': ['grass', 'orchard'],
                'natural': ['island', 'wood'],
                'leisure': 'park'
            }
        },
        'scrub'    : {
            'tags': {
                'natural': 'scrub'
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
            }
        },
        'garden'   : {
            'tags': {
                'leisure': ['garden', 'pitch']
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
                'natural': ['beach', 'heath']
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
        'forest'    : {
            'fc'    : '#64B96A',
            'ec'    : '#2F3737',
            'lw'    : 1,
            'zorder': 1
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
