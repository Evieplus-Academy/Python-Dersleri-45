import re

pattern = ".er.a."
text = "ezgi, ferhat, serkan, ferhat, büşra ve serhat"

matches = re.findall(pattern, text)
print(matches)

pattern = "ab*c"    # ac abc abbc abbbc abbbbc ...
text = "asd abc ac abbc abbbbc xdfrg rgfd abbbc"

matches = re.findall(pattern, text)
print(matches)

pattern = "ab+c"    # abc abbc abbbc abbbbc ...
text = "asd abc ac abbc abbbbc xdfrg rgfd abbbc"

matches = re.findall(pattern, text)
print(matches)

pattern = "ab?c"    # ac abc
text = "asd abc ac abbc abbbbc xdfrg rgfd abbbc"

matches = re.findall(pattern, text)
print(matches)

pattern = "ab{1,3}c"
text = "asd abc ac abbc abbbbc xdfrg rgfd abbbc"

matches = re.findall(pattern, text)
print(matches)

pattern = "ab[a-fA-Fç]c"
text = "asd abc ac abbc abbbbc abEc abçc xdfrg abfc rgfd abbbc abac abcc"

matches = re.findall(pattern, text)
print(matches)

pattern = "ab{1,3}c|ab[a-fA-Fç]c"
text = "asd abc ac abbc abbbbc abEc abçc xdfrg abfc rgfd abbbc abac abcc"

matches = re.findall(pattern, text)
print(matches)


pattern = "(ab)+c"  # abc ababc abababc
text = "asd abc ababc abababc ac abbc abbbbc abEc abçc xdfrg abfc rgfd abbbc abac abcc"

matches = re.findall(pattern, text)
print(matches)
