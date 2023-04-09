import re


pattern = r"\b\w+\b"
word_count_pattern = re.compile(pattern)
text1 = "Python öğrenmek çok kolaydır. Program yazmak daha da kolaydır."
text2 = "C++ ile gömülü sistemler için kod yazılır."

matches = word_count_pattern.findall(text1)
print(len(matches))
matches = word_count_pattern.findall(text2)
print(len(matches))

matches = word_count_pattern.finditer(text1)
for match in matches:
    print(match)
