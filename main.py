from itertools import combinations, product
import csv


_colors = [
    (0.0, 0.0, 0.0, 1), #rgba(0,0,0),
    (0.3607843137254902, 0.6352941176470588, 0.8313725490196079, 1), #rgba(143,252,255)
    (0.2196078431372549, 0.3803921568627451, 0.9725490196078431, 1), #rgba(56, 97, 248)
    (0.27450980392156865, 0.15294117647058825, 0.6862745098039216, 1), #rgba(70, 39, 175)
    (0.7803921568627451, 0.24313725490196078, 0.4666666666666667, 1), #rgb(199, 62, 119)
    (0.8666666666666667, 0.25882352941176473, 0.11372549019607843, 1), #rgb(221, 66, 29)
    (0.8823529411764706, 0.41568627450980394, 0.12941176470588237, 1), #rgb(225, 106, 33)
    (0.9921568627450981, 0.9882352941176471, 0.33725490196078434, 1), #rgb(253, 252, 86)
    (0.5529411764705883, 0.7294117647058823, 0.30196078431372547, 1), #rgb(141, 249, 75)
]

colors = list(product(_colors, repeat = 2))

scales = [
    (0.9, 1.2, 1.2), #tron
    (0.8, 0.6, 1.5), #nhon doc
    (0.9, 1.3, 0.9), #nhon ngang
    (1.3, 1.3, 0.5) # phang face tren
]

emissions = [5, 30]
voronois = [5, 10]
displacement = [0.02, 0.1, 0.4]

data = list(product(scales, colors, emissions, voronois, displacement))


fields = ['scale', 'color', 'emission', 'voronoi', 'displacement']
with open('GFG.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(data)





