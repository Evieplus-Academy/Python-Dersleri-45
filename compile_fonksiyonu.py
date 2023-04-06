import re

raw_pattern = "abc"
pattern = re.compile(raw_pattern)

text = "abc bca 123 xyz abc fgh"

matches = pattern.findall(text)
print(matches)

text = "kabcf abcfgh abc"
match = pattern.search(text)
print(match.start())

text = "kdjfhgjfabcjdhf jfjfkd"
text = pattern.sub(" ", text)
print(text)

text = "adlkfladkhfabcsldkfjweıabcdflksdjfabc"
result = pattern.split(text)
print(result)
