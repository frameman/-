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