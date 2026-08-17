from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="en")
print(hasattr(ocr, "predict"))
print(hasattr(ocr, "ocr"))