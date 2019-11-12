from __future__ import print_function
import argparse
import random
import torch
from torch.autograd import Variable
from PIL import Image
import tensorflow as tf

import numpy as np
from torchvision.transforms import Compose, CenterCrop, ToTensor, Resize, RandomCrop

# Training settings
parser = argparse.ArgumentParser(description='PyTorch Super Res Example')
parser.add_argument('--input_image', type=str, required=True, help='input image to use')
parser.add_argument('--output_filename', type=str, help='where to save the output image')
opt = parser.parse_args()

print(opt)
img = Image.open(opt.input_image).convert('RGB')

w,h  = img.size

for hi in range(4):
    for vi in range(2):

        x = w/4 * hi
        y = h/2 * vi

        crop_img = img.crop(( x,y, x+w/4 , y+h/2))

        dir = opt.output_filename.split('.')[0]
        base = opt.output_filename.split('.')[1]
        ext  = opt.output_filename.split('.')[2]
        out_name = "." + dir + base + "_" + '{:03d}'.format(vi*4+hi) +"." + ext

        print('output image saved to ', out_name)

        crop_img.save(out_name)
