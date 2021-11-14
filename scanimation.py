import cv2
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help='the input directory containing images')
parser.add_argument('--threshold', help='the threshold to be applied for image binarization.', default=127)


args = parser.parse_args()

directory = args.dir
threshold = args.threshold

imgs = []
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(filename)
        img_path = os.path.join(directory, filename)
        img = cv2.imread(img_path, 0)
        ret, img = cv2.threshold(img,threshold, 255, cv2.THRESH_BINARY)
        imgs.append(img)


step = 1
stride = step * len(imgs)
num_strides = imgs[0].shape[1] // stride
output_img = np.zeros(imgs[0].shape, dtype=np.uint8)

img_size = imgs[0].shape
for i in range(0, num_strides):
    for j in range(0, len(imgs)):        
        output_img[0:img_size[0], i*stride+j*step:i*stride+(j+1)*step] = imgs[j][0:img_size[0], i*stride+j*step:i*stride+(j+1)*step]

cv2.imwrite("output.png", output_img)

strides_img = np.zeros(imgs[0].shape, dtype=np.uint8)
for i in range(0, num_strides):
    strides_img[0:img_size[0], i*stride:i*stride+step] = np.ones((img_size[0], step), dtype=np.uint8) * 255  

cv2.imwrite("strides.png", strides_img)