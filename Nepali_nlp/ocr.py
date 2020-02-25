import sys
sys.path.append('..')

from PIL import Image
import pytesseract
import cv2
import os


def OCR(image,lang='nep', colab=False):
    """This function helps to generate text from image
    
    Arguments:
        image {string} -- [Location of image.]
    
    Keyword Arguments:
        lang {str} -- [language for OCR] (default: {'nep'})
    
    Returns:
        [string] -- [Text generated by OCR.]
    """
    assert lang in ['eng','nep'], 'specified language is not available at the moment'

    if not colab:
        image = cv2.imread(image)
        image = cv2.cvtColor(image, cv2.COLOR_BRG2GRAY)

    if lang=='nep':
        tessdata_dir_config = r'--tessdata-dir "local_dataset"'
        text = pytesseract.image_to_string(image, lang=lang, config=tessdata_dir_config)
        
        return text
    
    text = pytesseract.image_to_string(image)#if 'eng' is the choice
    return text