import cv2
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='PyTorch Super Res Example')

parser.add_argument('--input_image', type=str, required=True, help='input image to use')
parser.add_argument('--output_filename', type=str, help='where to save the output image')
opt = parser.parse_args()

image = cv2.imread(opt.input_image)
width,height,channels  = image.shape


image_half = cv2.resize(image,dsize=(0,0),fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

gaussian      = cv2.GaussianBlur(image,     (9,9), 10.0)
gaussian_half = cv2.GaussianBlur(image_half,(5,5), 10.0)

hf_image      = cv2.subtract(image     , gaussian     )
hf_image_half = cv2.subtract(image_half, gaussian_half)

hf_half_to_original = cv2.resize(hf_image_half,dsize=(0,0),fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)

b,  g,  r, _ = cv2.mean(abs(hf_image))
b2, g2, r2,_  = cv2.mean(abs(hf_half_to_original))

if(b+g+r == 0) :
    alpha = 0
else :
    alpha = (float)(b2+g2+r2) /(float)(b+g+r)

print(alpha)


