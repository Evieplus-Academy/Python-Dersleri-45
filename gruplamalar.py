import re


pattern = r"\b(\d{2})[.-](\d{2})[.-](\d{4})\b"
text = "Bugün 09.04.2023. Yarın 10-04-2023."

matches = re.findall(pattern, text)
for match in matches:
    print(match)

pattern = r"(?P<ssl>https?)://[a-zA-Z.]+"
text = "sitelerimiz https://www.sitem.com ve http://www.siten.edu"
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())
    if match.group("ssl") == "https":
        print("SSL kullanılıyor")

pattern = r"\b(?P<day>\d{2})[.-](?P<month>\d{2})[.-](?P<year>\d{4})\b"
text = "Bugün 09.04.2023. Yarın 10-04-2023."

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group("day"), match.group("month"), match.group("year"))

pattern = r"\b(\w+)\s\1\b"
text = "Ben kekeme olduğumdan durmadan selam selam naber naber diyorum."

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())

pattern = r"Python(?!rocks)"
text = "Pythonrocks is fun. Pythonista is awesome."

match = re.search(pattern, text)
print(match.group(), match)

pattern = r"(?<!Python)script"
text = "Pythonscript is fun. Pythonista is awesome. Javascript is cute."

match = re.search(pattern, text)
print(match.group(), match)

pattern = r"\b(\d{2})[.-](\d{2})[.-](\d{4})\b"
replacement = r"\3/\2/\1"
text = "Bugün 09.04.2023. Yarın 10-04-2023."

new_text = re.sub(pattern, replacement, text)
print(new_text)
