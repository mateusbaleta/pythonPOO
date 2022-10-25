import os
import sys
import argparse
from PIL import Image


# Parse args
parser = argparse.ArgumentParser(
    description='Image Converter\n--By BraiNiac--')
parser.add_argument(
    '-p',
    type=str,
    metavar='<Folder path>',
    help='Path to file'
)
parser.add_argument(
    '-f',
    type=str,
    metavar='<JPG/PNG/GIF/ICO/BMP>',
    help='Image output format: JPG/PNG/GIF'
)
parser.add_argument(
    '-o',
    type=str,
    metavar='<Output folder path>',
    help='Create output file folder on desired path'
)

# Get args
args = parser.parse_args()
p = args.p
f = args.f.lower()
o = args.o


# Converter
# check is new/exists, if not create it
if os.path.exists(o) is True:
    print('Folder already exists, '
          'choose another folder name.')
    sys.exit()
else:
    os.makedirs(o)

# loop through Pokedex, convert images
for filename in os.listdir(p):
    img = Image.open(f'{p}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{o}{clean_name}.{f}', f)
    print('Done! -->', clean_name)
else:
    parser.print_help()
    sys.exit()
