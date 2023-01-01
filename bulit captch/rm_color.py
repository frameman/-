import random
class create_color:
    def Random_color():
        r = random.randint(0,70) #use darker color so that it easy to recongize
        g = random.randint(0,70)
        b = random.randint(0,70)
        return (r,g,b)
    