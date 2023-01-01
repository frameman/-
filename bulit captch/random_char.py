import random


class create_a_random_string:
    def getRandomString():
        random_num = str(random.randint(0,9)) # random number min 0 max 9
        random_lchar= chr(random.randint(97,122)) #小寫字母a~z
        random_uchar = chr(random.randint(65,90)) # 大寫字母A~Z
        random_string = random.choice([random_num,random_lchar,random_uchar]) 
        #random pick a char fromrandom_num,random_lchar,random_uchar
        return random_string
    print(getRandomString())