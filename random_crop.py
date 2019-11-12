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
parser.add_argument('--model', type=str, required=True, help='model file to use')
parser.add_argument('--output_filename', type=str, help='where to save the output image')
parser.add_argument('--cuda', action='store_true', help='use cuda')
opt = parser.parse_args()

print(opt)
img = Image.open(opt.input_image).convert('RGB')

output_size = 256
w,h  = img.size
th, tw = 256, 256

for multinum in range(100):
    rx = random.randint(0, w-tw)
    ry = random.randint(0, h-th)

    crop_img = img.crop(( rx,ry, rx+tw , ry+th))

    dir = opt.output_filename.split('.')[0]
    base = opt.output_filename.split('.')[1]
    ext  = opt.output_filename.split('.')[2]
    out_name = "." + dir + base + "_" + '{:03d}'.format(multinum) +"." + ext

    print('output image saved to ', out_name)

    crop_img.save(out_name)
