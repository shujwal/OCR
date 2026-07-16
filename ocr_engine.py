from paddleocr import PaddleOCR
import cv2

# Create OCR object once.
# This saves time because the model loads only once.
ocr = PaddleOCR(
    use_doc_orientation_classify=True,
    use_textline_orientation=True,
    lang="en"
)

# ocr = PaddleOCR(
#     lang="ne",
#     ocr_version="PP-OCRv5",
#     use_doc_orientation_classify=True,
#     use_textline_orientation=True,
#     use_doc_unwarping=False
# )



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
# def preprocess(image_path):
#     image = cv2.imread(image_path)

#     # Upscale
#     image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Reduce noise
#     gray = cv2.GaussianBlur(gray, (3, 3), 0)

#     # Improve contrast
#     gray = cv2.equalizeHist(gray)

#     # Adaptive threshold
#     gray = cv2.adaptiveThreshold(
#         gray,
#         255,
#         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#         cv2.THRESH_BINARY,
#         11,
#         2
#     )

#     # Convert back to 3 channels
#     processed = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

#     return processed



def read_document(image_path):
    """
    Reads an image using PaddleOCR.

    Returns:
        raw_text -> Complete detected text
        ocr_result -> Full PaddleOCR output
    """

    grey = preprocess(image_path)
    result = ocr.predict(grey)

    detected_lines = []

    # Loop through detected text
    for page in result:

        if "rec_texts" not in page:
            continue

        for text in page["rec_texts"]:
            detected_lines.append(text)

    raw_text = "\n".join(detected_lines)

    return raw_text, result