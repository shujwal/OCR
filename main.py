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


# # Can use local ai model for Ocr text correction and attribute field detection
# # this approach makes the fields extraction easy but may be difficult to setup initially
# import ollama
# response = ollama.chat(
#     model="hermes3",
#     messages=[
#         {
#             "role": "user",
#             "content": f"""
#             You are an OCR correction assistant for Nepali government documents.

#               Rules:
#             - Correct OCR mistakes only.
#             - Do not translate.
#             - Do not summarize.
#             - Do not remove any information.
#             - Preserve line order.
#             - Preserve both English and Nepali words.
#             - Preserve numbers exactly.
#             - Return only the corrected text.

#             OCR Text:

#             {raw_text} """
#         }
#     ]
# )

# corrected_text = response["message"]["content"]