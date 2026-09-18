def get_ocr_stats(text):
    """
    Return basic statistics about OCR output.
    """

    if not text:
        return {
            "characters": 0,
            "words": 0,
            "lines": 0
        }

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    words = text.split()

    return {
        "characters": len(text),
        "words": len(words),
        "lines": len(lines)
    }


if __name__ == "__main__":
    sample_text = """Nepal Government
Citizenship Certificate
Bibash Pandey"""

    stats = get_ocr_stats(sample_text)

    print("OCR Statistics")
    print(f"Characters: {stats['characters']}")
    print(f"Words: {stats['words']}")
    print(f"Lines: {stats['lines']}")
