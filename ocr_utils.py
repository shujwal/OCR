import re


def clean_ocr_text(text):
    """
    Clean raw text returned by an OCR engine.

    Removes extra spaces and blank lines while
    keeping the original text content.
    """

    if not text:
        return ""

    lines = []

    for line in text.splitlines():
        line = line.strip()
        line = re.sub(r"\s+", " ", line)

        if line:
            lines.append(line)

    return "\n".join(lines)


def normalize_field_text(text):
    """
    Normalize a single OCR field value.
    """

    if not text:
        return ""

    text = text.strip()
    text = re.sub(r"\s+", " ", text)

    return text