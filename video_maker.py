import cv2
import numpy as np
import glob

videos = ['root_call_id']

for video in videos:
    img_array = []
    for filename in glob.glob(f'{video}/*.png'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter(f'{video}_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
