import re


pattern = r"\d{10}"
text = "5336659992 5326659992 5346659992 532"

matches = re.findall(pattern, text)
print(matches)

pattern = r"\D{10}"
text = "5336659992 5326659992 5346659992 532 skjdfh!*sd"

matches = re.findall(pattern, text)
print(matches)

pattern = r"\w{10}"
text = "5336659992 5326659992 5346659992 532 skjdfh__sd"

matches = re.findall(pattern, text)
print(matches)

pattern = r"\W{3}"
text = "5336659992 !!! 5326659992 5346659992_*?* 532 skjdfh__sd"

matches = re.findall(pattern, text)
print(matches)

pattern = r"\s{3}"
text = "5336659992 !!!   5326659992\n\n\n5346659992\t\t\t\t*?* 532 skjdfh__sd"

matches = re.findall(pattern, text)
print(matches)

pattern = r"\S{3,10}"
text = "5336659992 !!!   5326659992\n\n\n5346659992\t\t\t\t*?* 532 skjdfh__sd"

matches = re.findall(pattern, text)
print(matches)
