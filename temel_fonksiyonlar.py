import re


pattern = r"abc"
text = "xyz abc zyx"

match = re.search(pattern, text)
print(match)
if match:
    print("buldum", match.span(), match.group(), match.start(), match.end())
else:
    print("bulamadım")

pattern = r"abc"
text = "abc xyz abc zyx"

match = re.match(pattern, text)
print(match)
if match:
    print("buldum", match.span(), match.group(), match.start(), match.end())
else:
    print("bulamadım")

pattern = r"abc"
text = "abc xyz abc zyx"

matches = re.findall(pattern, text)
print(matches)
if matches:
    print("buldum")
else:
    print("bulamadım")


pattern = r"axbc"
text = "abc xyz abc zyx axbc"

matches = re.finditer(pattern, text)
print(matches)
for match in matches:
    print(match, match.group())


pattern = r"abc"
text = "abc xyz abc zyx axbc"

new_text = re.sub(pattern, "XXX", text)
print(new_text)


pattern = r"abc"
text = "abc xyz abc zyx axbc abc"

splited_list = re.split(pattern, text)
print(splited_list)
