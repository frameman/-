
from PIL import Image
import pytesseract

def main():
    pytesseract.pytesseract.tesseract_cmd = r'D:\\OCR\\tesseract.exe'
    #img = Image.open('C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\bg\\pic0.png') 
    img = Image.open('C:\\Users\\tom12\\Desktop\\ict\\captch\\result\\test\\pepper_noice\\peppersalt0.jpg') 
    text = pytesseract.image_to_string(img, lang='eng')
    print(text)
main()