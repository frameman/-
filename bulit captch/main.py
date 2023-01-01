
import cv2
import random
import os
from PIL import Image, ImageDraw, ImageFont
from matplotlib.pyplot import draw
import numpy as np

from gaussian import gaussian
from rm_color import create_color
from random_char import create_a_random_string
from salt import salt
from 加入曲線 import add_line



class main:
    id_i=0
    def bg(id_i):
        # random a background color 
        #bg_color = create_bg_color.Random_color() 
        #color = random.randint(0,5000)
        
        #create a new image with width 160,height 50  background_color gainsboro
        img = Image.new(mode ='RGB',size = (160,50),color='gainsboro')
       
        #add font 
        font_ ="C:\\Users\\tom12\\Desktop\\ict\\captch\\upckbi.ttf"
        draw = ImageDraw.Draw(img)                                  
        font = ImageFont.truetype(font=font_,size =random.randint(40,50))
        
        # add char on to img
        for i in range(5):
            ran_text = create_a_random_string.getRandomString()
            txt_color = create_color.Random_color()
            #the char and bg will not be the same color
            # while txt_color == bg_color:
            #     txt_color = create_bg_color.Random_color()
            draw.text((25+23*i,7),text=ran_text,fill=txt_color,font=font)
        
        first = 'C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\bg\\pic'+str(id_i)+'.png'
        with open(first,'wb') as f:
            img.save(f,format='png')
        #dots.drawPoint(draw)
        
        add_line.drawLine(draw)

        # output img
        no_noice_img_path = 'C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\no noice\\pic'+str(id_i)+'.png'
        with open(no_noice_img_path,'wb') as f:
            img.save(f,format='png')

        
        pic = 'C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\no noice\\pic'+str(id_i)+'.png'
        img = cv2.imread(pic)
        
        #add pepper_salt to the img
        salt.salt_add(img,id_i)
        #add gaussian_noice to the img
        gaussian.gausss(img,id_i)
    
    while id_i<=20:
        bg(id_i)
        id_i+=1