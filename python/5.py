import pytesseract
from PIL import Image

tessdata_dir_config = '--tessdata-dir "D:\\Tesseract-OCR\\tessdata"'
image=Image.open('C:\\Users\\w2239\\Desktop\\图片\\32.jpg')
code=pytesseract.image_to_string(image,config=tessdata_dir_config)
print(code)