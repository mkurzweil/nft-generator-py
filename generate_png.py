import os
import glob
import random

from PIL import Image
from config import * # variable and path config
from duplicate_check_png import *
from duplicate_check_png import *

# delete backgrounds from folder
files = glob.glob('trait-layers/backgrounds/collection/*')
for f in files:
    os.remove(f)

for i in range(number_of_png):
    # generate random numbers
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    weights = random.randint(10,90)

    # create img and store it to file system
    img = Image.new( mode = "RGB", size = (width, height), color = (r, g, b) )
    img.save(os.path.join(out_dir, 'background_' + str(i) + '.png'))

    # TODO: comparison not working.
    duplication_check()

    if i == number_of_png-1:
        layers_values += '"Background_' + str(i) + '" '
        layers_filename += '"background_' + str(i)  + '" '
        layers_weight += '' + str(weights) + ''
    else:
        layers_values += '"Background_' + str(i) + '", '
        layers_filename += '"background_' + str(i)  + '", '
        layers_weight += '' +  str(weights) + ', '



layers_values += '],'
layers_filename += '],'
layers_weight += ']'
print('\n')
# copy output to index.py
print('Just copy&paste to index.py:')
print('{')
print('"name": "Background",')
print(layers_values)
print('"trait_path": "./trait-layers/backgrounds",')
print(layers_filename)
print(layers_weight)
print('}')