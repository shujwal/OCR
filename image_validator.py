from pathlib import Path
import cv2


SUPPORTED_FORMATS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def validate_image(image_path):
    """
    Validate an image before sending it to the OCR pipeline.

    Returns:
        tuple: (is_valid, message)
    """

    path = Path(image_path)

    if not path.exists():
        return False, "Image file does not exist."

    if not path.is_file():
        return False, "The provided path is not a file."

    if path.suffix.lower() not in SUPPORTED_FORMATS:
        return False, f"Unsupported image format: {path.suffix}"

    image = cv2.imread(str(path))

    if image is None:
        return False, "Image could not be read."

    height, width = image.shape[:2]

    if width == 0 or height == 0:
        return False, "Image has invalid dimensions."

    return True, f"Valid image: {width}x{height}"


if __name__ == "__main__":
    image_path = "sample_images/nepali-citizenship-card-front.jpg"

    valid, message = validate_image(image_path)

    print(message)