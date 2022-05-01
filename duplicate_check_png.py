from PIL import Image
from config import * # variable and path config

import glob
import os

def duplication_check():
    for img in glob.glob(str(current_dir / "*.png")):
            filename = Image.open(img)
            colors = filename.getpixel((1, 1))

            # TODO: comparison not working
            if r == colors[0] and g == colors[1] and b == colors[2]:
                print("same img - delete it")
                os.remove(filename)
            else:
                print("no image file duplication")