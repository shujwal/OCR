from paddleocr import PaddleOCR

try:
    PaddleOCR(lang="latin")
    print("latin works..")
except Exception as e:
    print(e)

try:
    PaddleOCR(lang="devanagari")
    print("devanagari works..")
except Exception as e:
    print(e)

from paddleocr import PaddleOCR



ocr = PaddleOCR(lang="ne", ocr_version="PP-OCRv5")    