import re

pattern1 = "^abc"
pattern2 = "abc$"
pattern3 = r"abc\b"
pattern4 = r"\Babc"
text = "abc abcdef defabc abcdef abc123 123abc abc"

matches = re.findall(pattern4, text)
print(matches)
