
import cv2
import numpy as np
from add_id import add_id
class gaussian:
    def gausss(img,i):
        i = add_id.pic_id(i)
        gauss = np.random.normal(0,.8,img.size)
        gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
        img_gauss = cv2.add(img,gauss)
        
        
        file_name = 'C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\gaussian_noice\\gaussian'+str(i)+'.png' 
        cv2.imwrite(file_name,img_gauss)