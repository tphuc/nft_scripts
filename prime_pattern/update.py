import csv 
import os
import re

mypath = '../../texture/'
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

_lines = [i.split('.')[0] for i in onlyfiles]
_lines.remove('') 
lines = [int(i) for i in _lines]

with open("shape.csv") as f:
    csv_reader = csv.reader(f, delimiter=',')
    data = list(csv_reader)
    newData = []

    for line in lines:
        index = line - 1
        newData.append(data[index])


    with open('shape_update.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(newData)
