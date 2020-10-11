# -*- coding: utf-8 -*-

# system
import sys
import os
import argparse
# image processing
import matplotlib.pyplot as plt
from matplotlib import image
from PIL import Image


parser = argparse.ArgumentParser(description="image-resize")

parser.add_argument('--scale', dest='sc', type=float, metavar='scale', required=False)
parser.add_argument('--size', dest='sz', nargs=2, type=int, metavar='size', required=False)
parser.add_argument('--path', dest='p', type=str, metavar='path', required=True)
parser.add_argument('--filename', dest='fn', type=str, metavar='filename', required=False, default='output.jpg')
args = parser.parse_args()

mode = None

if args.sc:
    scale = args.sc
    mode = 'scale'

if args.sz:
    size = (args.sz[0], args.sz[1])
    mode = 'size'

if (args.sc and args.sz) or (not args.sc and not args.sz):
    print('Please specify positive sclae OR positive size')
    exit()

path = args.p
filename = args.fn

# reduce size of image:
im = Image.open(path)
s = im.size

if mode == 'scale':
    im = im.resize((int(s[0] * scale), int(s[1] * scale)), Image.ANTIALIAS)
elif mode == 'size':
    im = im.resize((size[0], size[1]), Image.ANTIALIAS)
else:
    print('Error')

im.save(filename)
