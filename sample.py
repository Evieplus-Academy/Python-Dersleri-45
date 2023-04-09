import re

with open("sample.txt", "r", encoding="utf-8") as file_object:
    text = file_object.read()

pattern = r"\b[uU][fF][oO]\b"
text_censored = re.sub(pattern, "SANSÜRLÜ", text)

with open("sample_censored.txt", "w", encoding="utf-8") as file_object:
    file_object.write(text_censored)

print("'sample_censored.txt' dosyası oluşturuldu.")

def replacement(match):
    turkish_to_latin = {
        "ğ": "g",
        "Ğ": "G",
        "ı": "i",
        "İ": "I",
        "ş": "s",
        "Ş": "S",
        "ü": "u",
        "Ü": "U",
        "ö": "o",
        "Ö": "O",
        "ç": "c",
        "Ç": "C"
    }
    return turkish_to_latin[match.group()]


with open("sample.txt", "r", encoding="utf-8") as file_object:
    text = file_object.read()

pattern = r"[ğĞıİşŞüÜöÖçÇ]"
new_text = re.sub(pattern, replacement, text)

with open("sample.new.txt", "w", encoding="utf-8") as file_object:
    file_object.write(new_text)
    
