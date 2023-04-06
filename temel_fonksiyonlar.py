import re

pattern = "xyz"
replace_with = "FERHAT"
text = "xyz abc 123 xyz"

print(text)
text = re.sub(pattern, replace_with, text)
print(text)

pattern = "HAT"
matches = re.findall(pattern, text)
print(matches)



