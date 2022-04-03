from pathlib import Path

# Number for PNG file generation
number_of_png = 10

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
out_dir = current_dir / "trait-layers/backgrounds/collection"

# json string
layers_values = '"values" : ['
layers_filename = '"filename" : ['
layers_weight = '"weights": ['