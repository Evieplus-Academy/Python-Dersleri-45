import re

with open("sample.txt", "r", encoding="utf-8") as file_object:
    text = file_object.read()

pattern = r"\b[uU][fF][oO]\b"
text_censored = re.sub(pattern, "SANSÜRLÜ", text)

with open("sample_censored.txt", "w", encoding="utf-8") as file_object:
    file_object.write(text_censored)

print("'sample_censored.txt' dosyası oluşturuldu.")
