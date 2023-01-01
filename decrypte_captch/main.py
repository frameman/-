from matplotlib import pyplot as plt
import cv2
import numpy as np
import os 
import fnmatch 
pic = fnmatch.filter(os.listdir('C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\pepper_noice'),"*.jpg")

def gray(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    file_name = 'C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\gray_img\\gray_'+i
    cv2.imwrite(file_name,img)
    return img


def Binarization(img): #二值化
    ret, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    file_name = 'C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\binariztaion\\bin_'+i
    cv2.imwrite(file_name,img)
    return img

def blur_img(img):
    kernel = 1/16*np.array([[1,2,1],[2,4,2],[1,2,1]])
    img_blur = cv2.filter2D(img,-1,kernel)
    file_name = 'C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\blur\\blur_'+i
    cv2.imwrite(file_name,img_blur)
    return img_blur

def remove_line(img,i):
    ret,img= cv2.threshold(img,140,255,cv2.THRESH_BINARY)
    kernel =np.ones((2,2),np.uint8)
    img = (cv2.dilate(img,kernel,iterations=1))
    file_name = 'C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\finial\\'+i
    cv2.imwrite(file_name,img)

for i in pic:
   
    img = cv2.imread('C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\pepper_noice\\'+i)
    img_gray = gray(img)
    img_bin =Binarization(img_gray)
    img_blur = blur_img(img_bin)
    finial_img = remove_line(img_blur,i)

