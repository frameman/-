import random
from rm_color import create_bg_color
class dots:
    def drawPoint(draw):
        for i in range(600):
            x = random.randint(0, 160)
            y = random.randint(0, 50)
            draw.point((x,y), fill= create_bg_color.Random_color())