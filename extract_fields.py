# def get_value(lines, current_index):
#     """
#     Get the value from the same line after ':'.
#     If empty, return the next non-empty line.
#     """

#     line = lines[current_index].strip()

#     if ":" in line:
#         value = line.split(":", 1)[1].strip()
#         if value:
#             return value

#     for i in range(current_index + 1, len(lines)):
#         value = lines[i].strip()
#         if value:
#             return value

#     return ""

def get_value(lines, i):
    # Same line
    if ":" in lines[i]:
        value = lines[i].split(":", 1)[1].strip()
        if value:
            return value

    labels = [
        "Citizenship Certificate No.",
        "Full Name",
        "Sex",
        "Date of Birth",
        "Year",
        "Month",
        "Day",
        "Place of Birth",
        "Permanent Address",
        "District",
        "Municipality",
        "VDC",
        "Ward",
        "Father",
        "Mother",
        "Spouse",
        "ना.प्र.नं.",
        "नाम",
        "जन्मस्थान",
        "जन्ममिति",
        "स्थायी बसोबास",
        "गा./न.पा.",
        "गा.पा.",
        "न.पा.",
        "बाबुको",
        "आमाको",
        "पति",
        "पत्नी"
    ]

    # Check next few lines
    for j in range(i + 1, min(i + 4, len(lines))):
        text = lines[j].strip()

        if not text:
            continue

        # Skip field labels
        if any(text.startswith(label) for label in labels):
            continue

        return text

    return ""


def extract_citizen_front_nepali(raw_text):

    fields = {
        "citizenship_number": "",
        "full_name": "",
        "birth_place": "",
        "permanent_address": "",
        "address": "",
        "date_of_birth": "",
        "father_name": "",
        "mother_name": "",
        "spouse_name": ""
    }

    lines = raw_text.split("\n")

    for i, line in enumerate(lines):

        line = line.strip()

        if "ना.प्र.नं." in line:
            fields["citizenship_number"] = get_value(lines, i)

        elif line.startswith("नाम"):
            fields["full_name"] = get_value(lines, i)

        elif line.startswith("जन्मस्थान"):
            fields["birth_place"] = get_value(lines, i)

        elif line.startswith("स्थायी बसोबास"):
            fields["permanent_address"] = get_value(lines, i)

        elif line.startswith("गा./न.पा.") or line.startswith("गा.पा.") or line.startswith("न.पा."):
            fields["address"] = get_value(lines, i)

        elif line.startswith("जन्ममिति"):
            fields["date_of_birth"] = get_value(lines, i)

        elif line.startswith("बाबुको"):
            fields["father_name"] = get_value(lines, i)

        elif line.startswith("आमाको"):
            fields["mother_name"] = get_value(lines, i)

        elif line.startswith("पति") or line.startswith("पत्नी"):
            fields["spouse_name"] = get_value(lines, i)

    return fields


def extract_citizen_front_english(raw_text):

    fields = {
        "citizenship_number": "",
        "full_name": "",
        "sex": "",
        "date_of_birth": "",
        "birth_district": "",
        "birth_municipality": "",
        "birth_ward": "",
        "father_name": "",
        "mother_name": "",
        "spouse_name": ""
    }

    lines = raw_text.split("\n")

    for i, line in enumerate(lines):

        line = line.strip()

        # Citizenship Number
        if "Citizenship Certificate No." in line:
            fields["citizenship_number"] = get_value(lines, i)

        # Full Name
        elif line.startswith("Full Name"):
            fields["full_name"] = get_value(lines, i)

        # Sex
        elif line.startswith("Sex"):
            fields["sex"] = get_value(lines, i)

        # Date of Birth
        elif "Date of Birth" in line:

            year = ""
            month = ""
            day = ""

            for j in range(i + 1, min(i + 6, len(lines))):

                current = lines[j].strip()

                if current.startswith("Year"):
                    year = current.split(":", 1)[1].strip()

                elif current.startswith("Month"):
                    month = current.split(":", 1)[1].strip()

                elif current.startswith("Day"):
                    day = current.split(":", 1)[1].strip()

            fields["date_of_birth"] = f"{year}-{month}-{day}"

        # Place of Birth
        elif "Place of Birth" in line:

            for j in range(i + 1, min(i + 6, len(lines))):

                current = lines[j].strip()

                if current.startswith("District"):
                    fields["birth_district"] = current.split(":", 1)[1].strip()

                elif current.startswith("Municipality") or current.startswith("VDC"):
                    fields["birth_municipality"] = current.split(":", 1)[1].strip()

                elif current.startswith("Ward"):
                    fields["birth_ward"] = current.split(":", 1)[1].strip()

        # Father
        elif line.startswith("Father"):
            fields["father_name"] = get_value(lines, i)

        # Mother
        elif line.startswith("Mother"):
            fields["mother_name"] = get_value(lines, i)

        # Spouse
        elif line.startswith("Spouse"):
            fields["spouse_name"] = get_value(lines, i)

    return fields