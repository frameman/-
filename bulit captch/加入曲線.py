import random
from rm_color import create_color
class add_line:
    def drawLine(draw):
        for i in range(5):
            x1 = random.randint(0, 160)  #x-axis starting point
            x2 = random.randint(0, 160)  #x-axis ending point
            y1 = random.randint(0, 50)   #y-axis starting point
            y2 = random.randint(0, 50)   #y-axis starting point
            draw.line((x1, y1, x2, y2), fill=create_color.Random_color())