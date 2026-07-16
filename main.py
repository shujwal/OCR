from ocr_engine import read_document
from extract_fields import *

image_path = "sample_images/mero_back_normal.jpeg"

raw_text, result = read_document(image_path)

fields = {}

if "नेपाल सरकार" in raw_text or "नाम" in raw_text:
    fields = extract_citizen_front_nepali(raw_text)

elif "Citizenship Certificate" in raw_text or "Full Name" in raw_text:
    fields = extract_citizen_front_english(raw_text)

else:
    print("Document type not recognized...")

print("\nRAW TEXT\n")
print(raw_text)

print("\nATTRIBUTES\n")
print(fields)