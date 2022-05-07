import bpy
import os
from os import listdir
from os.path import isfile, join
import csv

mypath = 'NFTs/images/'
onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
lastId = len(onlyfiles)


    

def render(id):
    # Render
    bpy.ops.render.render(write_still=1)
    # Save
    bpy.data.images['Render Result'].save_render(filepath= 'NFTs/' + str(id) + ".png")


def changeRGBs(first, second):
    bpy.data.materials["Material"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color = first
    bpy.data.materials["Material"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color = second



def changeSharpness(scale):
    # voronoi scale
    bpy.data.materials["Material"].node_tree.nodes["Voronoi Texture"].inputs[2].default_value = scale

def changeEmission(val):
    bpy.data.materials["Material"].node_tree.nodes["Emission"].inputs[1].default_value = val
    

def changeScale(val):
    bpy.data.objects["Icosphere"].select_set(True)
    bpy.ops.transform.resize(value=val, orient_type='LOCAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='LOCAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)


def changeDisplacement(scale):
    bpy.data.materials["Material"].node_tree.nodes["Displacement"].inputs[2].default_value = scale


def changeBackground(color):
    bpy.data.materials["Material"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color = color



def updateAll(scale, color, emission, tessellation, spikey):
    changeScale(eval(scale))
    changeRGBs(*eval(color))
    changeEmission(eval(emission))
    changeSharpness(eval(tessellation))
    changeDisplacement(spikey)



def create(n=100):
    with open("NFTs/scripts/nft.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        data = list(csv_reader)
        data = data[1:]
        print(data)
        for id in range(lastId, lastId+n):
            print('-- creating nft {}'.format(id))
            
create(n=1)