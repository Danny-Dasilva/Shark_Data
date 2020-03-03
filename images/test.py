

from PIL import Image
import cv2
import numpy as np

import json
import os
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_ext == ".jpg":
        print(file_name)


        img = f

        image = cv2.imread(img)
        height, width, channels = image.shape
        print(height, width)
        img = image



        with open('Label/' + file_name + '.txt') as f:
            t = f.readlines()
            for line in t:
                print(line)
                r = line.strip('\n').split(' ')
                print(r)
                y1 = float(r[1])
                x1 = float(r[2])
                x2 = float(r[3])
                y2 = float(r[4])


                cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),1)

        cv2.imshow('image',img)
        cv2.waitKey(0)
