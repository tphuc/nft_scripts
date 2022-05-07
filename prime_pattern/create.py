from itertools import combinations, product, permutations
import csv
from PIL import ImageColor
import json
import random

musgraves_scales = [2, 5, 10]
musgraves_detail = [1, 5,10]
musgraves_dimension = [0.8, 10]
musgraaves_lacunarit = [1,3]
noise_scale = [1, 5, 10]
noise_detail = [0, 5]




palletes = [
    ['#8386f5', '#3d43b4', '#041348', '#1afe49', '#083e12',], #neon
    ['#f887ff', '#29132e', '#de004e', '#860029', '#321450'], #neon
    ['#e96d5e', '#ff9760', '#6a7e6a', '#393f5f', '#ffe69d'], #vintage
    ['#ff124f', '#ff00a0', '#fe75fe', '#7a04eb', '#120458'], #neon
    ['#ff6e27',  '#fbf665', '#383e65', '#73fffe', '#6287f8'],#vintage
    ['#7700a6',  '#fe00fe', '#defe47', '#00b3fe', '#0016ee'],#neon
    ['#63345e', '#b7c1de', '#ac61b9', '#0b468c', '#092047'], #vibrant
    ['#af43b3', '#fd8090', '#c4ffff', '#08deea', '#1261d1'], #pastel
    ['#a0ffe3', '#8d8980', '#65dc98', '#575267', '#222035'], #vintage
    ['#ff2a6d', '#d1f7ff', '#05d9e8', '#005678', '#01012b'], #vibrant
    ['#8f704b', '#daae6d', '#4d9e9b', '#89e3f6', '#44786a'], #pastel
    ['#fdd870', '#d0902f', '#a15501', '#351409', '#fff69f'], #monochrome
    ['#b0acb0', '#3d898d', '#e2dddf', '#2f404d', '#85ebd9'], #monochrome
    ['#ff184c', '#ffccdc', '#ff477d', '#0a9cf5', '#003062'], #vibrant
    ['#6ac8d5', '#1d224c', '#67718f', '#d8d5d9', '#565fd6' ], #pastel
    ['#1c1a15', '#383345', '#CF9766',  '#E25D23', '#882717'], #vintage
    ['#010630', '#aae2fd', '#2476ad', '#5cabd5', '#053b7a'], #vibrant
    ['#e3ae08', '#13a7e1', '#fff2b8', '#0d2a53', '#ffdf30', ], #neon
    ['#00b4d8', '#caf0f8', '#03045e', '#90e0ef', '#0077b6'], #monochrome,
    ['#d88c9a', '#f2d0a9', '#99c1b9', '#f1e3d3', '#8e7dbe'] #pastel
]

def hex2rgb255(color):
    (r,g,b) = ImageColor.getrgb(color)
    return (r/255, g/255, b/255, 1)


# colors = list(product(musgraves_scales, musgraves_detail, musgraves_dimension, musgraaves_lacunarit, noise_scale, noise_detail))
colors = [ [hex2rgb255(color) for color in _colors] for _colors in palletes]


# data = list(product(musgraves_scales, musgraves_detail, musgraves_dimension, musgraaves_lacunarit, displacement))

# fields = ['scale', 'color', 'emission', 'voronoi', 'displacement']

with open('colors.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(colors)




meta = {
    'lacunary': { # musgraves lacunarit
        '1': 'I',
        '3': 'II'
    },
    'fractal': { #noise_scale
        '1': 'I',
        '5': 'II',
        '10': 'II'
    },
    'dissonant': { # musgraaves_dimension
        '0.8': 'II',
        '10': 'I'
    },
    'organic': {  # musgrave scale
        '2': 'I',
        '5': 'II',
        '10': 'III'
    },
    'pallete': {
        'neon': [
            ['#8386f5', '#3d43b4', '#041348', '#1afe49', '#083e12',],
            ['#f887ff', '#29132e', '#de004e', '#860029', '#321450'],
            ['#ff124f', '#ff00a0', '#fe75fe', '#7a04eb', '#120458'],
            ['#7700a6',  '#fe00fe', '#defe47', '#00b3fe', '#0016ee']
        ],
        'vintage': [
            ['#e96d5e', '#ff9760', '#6a7e6a', '#393f5f', '#ffe69d'],
            ['#ff6e27',  '#fbf665', '#383e65', '#73fffe', '#6287f8'],
            ['#a0ffe3', '#8d8980', '#65dc98', '#575267', '#222035'],
            ['#1c1a15', '#383345', '#CF9766',  '#E25D23', '#882717']
        ],
        'vibrant': [
            ['#63345e', '#b7c1de', '#ac61b9', '#0b468c', '#092047'],
            ['#ff2a6d', '#d1f7ff', '#05d9e8', '#005678', '#01012b'],
            ['#ff184c', '#ffccdc', '#ff477d', '#0a9cf5', '#003062'],
            ['#010630', '#aae2fd', '#2476ad', '#5cabd5', '#053b7a']
        ],
        'pastel': [
            ['#af43b3', '#fd8090', '#c4ffff', '#08deea', '#1261d1'],
            ['#8f704b', '#daae6d', '#4d9e9b', '#89e3f6', '#44786a'],
            ['#6ac8d5', '#1d224c', '#67718f', '#d8d5d9', '#565fd6' ]
        ],
        'monnochrome': [
            ['#fdd870', '#d0902f', '#a15501', '#351409', '#fff69f'],
            ['#b0acb0', '#3d898d', '#e2dddf', '#2f404d', '#85ebd9']
        ]
    },
    'colors': {
        "1": "neon",
        "2": "neon",
        "3": "vintage",
        "4": "neon",
        "5": "vintage",
        "6": "neon",
        "7": "vibrant",
        "8": "pastel",
        "9": "vintage",
        "10": "vibrant",
        "11": "pastel",
        "12": "monochrome",
        "13": "monochrome",
        "14": "vibrant",
        "15": "pastel",
        "16": "vintage",
        "17": "vibrant",
        "18": "neon",
        "19": "monochrome",
        "20": "pastel"
    }
}


def write(file, data):
    with open(file, 'w') as f:
        write = csv.writer(f)
        write.writerows(data)



def create_params():
    with open('shape_update.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        shapes = list(csv_reader)
        data = list(product(shapes, colors))
        print(len(data))
        
        write('params.csv', data)


def shuffle():
    with open("params.csv", 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        data = list(csv_reader)
        
        new_data = random.sample(data, len(data))
        write('data_shuffle.csv', new_data)
        


def write_meta():
    data = []
    with open("params_2.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        data = list(csv_reader)
    

    final_data = []
    for i, line in enumerate(data):
        item = {
            'name': 'PrimePattern #' + str(i+1),
            'description': 'Prime Pattern is a unique collection of 1260 computer generative abtract artworks on Polygon. Each abstract pattern is an exploration of colors, forms and shapes.',
            'attributes': [
                {
                    "trait_type": "Lacunary",
                    "value": ""
                },
                {
                    "trait_type": "Fractal",
                    "value": ""
                },
                {
                    "trait_type": "Dissonant",
                    "value": ""
                },
                {
                    "trait_type": "Organic",
                    "value": ""
                },
                {
                    "trait_type": "Palette",
                    "value": ""
                },
                {
                    "display_type":'number',
                    "trait_type": "Colors",
                    "value": ""
                }
            ]
        }
        _shape, _color = line;
        shape = eval(_shape)
        color = eval(_color)
        m_scale, m_detail, m_dimension, m_lacunarit, n_scale, n_detail = shape
        palette_id = colors.index(color) + 1
        item['edition'] = i + 1
        item['attributes'][0]['value'] = meta['lacunary'][m_lacunarit]
        item['attributes'][1]['value'] = meta['fractal'][n_scale]
        item['attributes'][2]['value'] = meta['dissonant'][m_dimension]
        item['attributes'][3]['value'] = meta['organic'][m_scale]
        item['attributes'][4]['value'] = meta['colors'][str(palette_id)]
        item['attributes'][5]['value'] = 5
        item['image'] = 'https://bafybeibbyohtmcwyfekhbe3mm7jz26h4rmxd4uhxds7apg2intiqkdzjkq.ipfs.nftstorage.link/{}.png'.format(i+1)

        with open('meta/{}.json'.format(i+1), 'w') as outfile:
            json.dump(item, outfile)




    
write_meta()