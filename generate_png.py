from PIL import Image
from pathlib import Path
import os
import random
import glob

# Number for PNG file generation
number_of_png = 100

# PNG pixel size
width = 1000
height = 1000

# RGB
r = 0
g = 0
b = 0

# layers -> nft generation
weights = 0

# current and output folder
current_dir = Path('.').resolve()
out_dir = current_dir / "trait-layers/backgrounds"

# json string
layers_values = '"values" : ['
layers_filename = '"filename" : ['
layers_weight = '"weights": ['


for i in range(number_of_png):
    # generate random numbers
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    weights = random.randint(10,90)

    # create img and store it to file system
    img = Image.new( mode = "RGB", size = (width, height), color = (r, g, b) )
    img.save(os.path.join(out_dir, 'background_' + str(i) + '.png'))

    # TODO: comparison not working
    for img in glob.glob(str(current_dir / "*.png")):
        filename = Image.open(img)
        colors = filename.getpixel((1, 1))

        # TODO: comparison not working
        if r == colors[0] and g == colors[1] and b == colors[2]:
            print("same img - delete it")
            os.remove(filename)
        else:
            print("no image file duplication")

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

# copy output to index.py
print('"name": "Background",')
print(layers_values)
print('"trait_path": "./trait-layers/backgrounds",')
print(layers_filename)
print(layers_weight)