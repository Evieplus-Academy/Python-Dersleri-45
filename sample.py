import re

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = re.compile(r'\b[Uu][Ff][Oo]\b')
text_censored = pattern.sub("SANSÜRLÜ", text)

with open("sample_censored.txt", "w", encoding="utf-8") as file:
    file.write(text_censored)

print("'sample_censored.txt' dosyası oluşturuldu.")
