import re

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = re.compile(r'\b[Uu][Ff][Oo]\b')
text_sansurlu = pattern.sub("SANSÜRLÜ", text)

with open("sample_sansurlu.txt", "w", encoding="utf-8") as file:
    file.write(text_sansurlu)

print("'sample_sansurlu.txt' dosyası oluşturuldu.")
