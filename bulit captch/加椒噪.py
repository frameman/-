import random
import cv2
import numpy as np
class salt_pepper:
    def add_salt_noise(image,prob):
        output = np.zeros(image.shape,np.uint8)
        thres = 1- prob
        for i in range(image.shape[0]):
           for j in range(image.shape[1]):
                randomum = random.random()
                if randomum <prob:
                   output[i][j] = 0
                elif (randomum>thres):
                    output[i][j] =255
                else:
                    output[i][j] = image[i][j]
        return output 
    img = cv2.imread('14876.png')
    add_salt_noise(img,prob=0.01)
    cv2.imwrite('C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\papasalt.png',img)
    