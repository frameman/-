from add_id import add_id
import cv2
import numpy as np
from skimage.util import random_noise
class salt:
    def salt_add(img,i):
        add_id.pic_id(i)
        noise_img = random_noise(img,mode='s&p',amount=0.07)
        noise_img =np.array(255*noise_img,dtype='uint8')
        file_name = 'C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\pepper_noice\\peppersalt'+str(i)+'.jpg'
        cv2.imwrite(file_name,noise_img)