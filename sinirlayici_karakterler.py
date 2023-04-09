import re


pattern = "^[a-f]bc"
text = "fbc bca abc"

matches = re.findall(pattern, text)
print(matches)

pattern = "[a-f]bc$"
text = "fbc bca abc"

matches = re.findall(pattern, text)
print(matches)


pattern = r"\b[a-f]b+c\b"
text = "fbc dbcc abbbbbc babca ggebc abc"

matches = re.findall(pattern, text)
print(matches)


pattern = r"\B[a-f]b+c\B"
text = "fbc dbcc abbbbbc babca ggebc abc"

matches = re.findall(pattern, text)
print(matches)
