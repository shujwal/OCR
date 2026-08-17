from paddleocr import PaddleOCR
import cv2

# Create OCR object once.
# This saves time because the model loads only once.
# ocr = PaddleOCR(  #this is for english
#     use_doc_orientation_classify=True,
#     use_textline_orientation=True,
#     lang="en")


# ocr = PaddleOCR(   #this is for nepali
#     lang="ne",
#     ocr_version="PP-OCRv5",
#     use_doc_orientation_classify=True,
#     use_textline_orientation=True,
#     use_doc_unwarping=False)
ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
)


    # 1st one
# def preprocess(image_path):
#     image = cv2.imread(image_path)

#     # Upscale 2x
#     image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Increase contrast
#     gray = cv2.equalizeHist(gray)

#     return gray


    # 2nd one
# def preprocess(image_path):
#     image = cv2.imread(image_path)

#     image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

#     return image



    #  3rd one
def preprocess(image_path):
    image = cv2.imread(image_path)

    # Resize 2x
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Light denoising
    image = cv2.fastNlMeansDenoisingColored(image, None, 5, 5, 7, 21)

    # CLAHE on grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)

    # Convert back to BGR
    processed = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    return processed



def read_document(image_path):
    """
    Reads an image using PaddleOCR.

    Returns:
        raw_text -> Complete detected text
        ocr_result -> Full PaddleOCR output
    """

    processed = preprocess(image_path)
    print(type(processed))
    print(processed is None)
    cv2.imwrite("debug_preprocessed.jpg", processed)
    result = ocr.ocr(processed, cls=True)
    print(result)
    # Loop through detected text
    detected_lines = []

    if result and result[0]:
        for line in result[0]:
            detected_lines.append(line[1][0])

    raw_text = "\n".join(detected_lines)

    return raw_text, result











# from PIL import Image

# from surya.recognition import RecognitionPredictor
# from surya.detection import DetectionPredictor

# # Load models once
# detector = DetectionPredictor()
# recognizer = RecognitionPredictor()


# def preprocess(image_path):
#     """
#     Surya works well on the original image.
#     No preprocessing is applied.
#     """
#     return Image.open(image_path).convert("RGB")


# def read_document(image_path):
#     """
#     Reads an image using Surya OCR.

#     Returns:
#         raw_text -> Complete detected text
#         result -> Full Surya result
#     """

#     image = preprocess(image_path)

#     # Detect text regions
#     detections = detector([image])

#     # Recognize text
#     results = recognizer([image], detections)

#     detected_lines = []

#     for page in results:
#         for line in page.text_lines:
#             detected_lines.append(line.text)

#     raw_text = "\n".join(detected_lines)

#     return raw_text, results