import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image


def main(name):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # читать изображение с помощью OpenCV
    image = cv2.imread("sts1.jpg")
    # image = cv2.imread("test.png")

    # получаем строку
    string = pytesseract.image_to_string(image, lang='rus+eng')
    # печатаем
    print(string)


if __name__ == '__main__':
    main('')
