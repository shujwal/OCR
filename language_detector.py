def detect_language(text):
    """
    Detect whether OCR text mainly contains
    Nepali or English characters.
    """

    if not text:
        return "unknown"

    nepali_count = 0
    english_count = 0

    for char in text:
        if "\u0900" <= char <= "\u097F":
            nepali_count += 1
        elif char.isascii() and char.isalpha():
            english_count += 1

    if nepali_count == 0 and english_count == 0:
        return "unknown"

    if nepali_count > english_count:
        return "nepali"

    if english_count > nepali_count:
        return "english"

    return "mixed"


if __name__ == "__main__":
    print("Nepali:", detect_language("नेपाल सरकार"))
    print("English:", detect_language("Government of Nepal"))
    print("Mixed:", detect_language("नेपाल Government"))
