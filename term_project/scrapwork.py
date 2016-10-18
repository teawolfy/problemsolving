import pytesseract
#import Image
#except ImportError:
from PIL import Image
from encodings import cp1252
original_decode  = cp1252.Codec.decode
cp1252.Codec.decode =  lambda self, input, errors="replace": original_decode(self, input, errors)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
print(pytesseract.image_to_string(Image.open('receipt1.jpg')))

