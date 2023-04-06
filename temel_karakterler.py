import re

pattern1 = "a.c"
pattern2 = "a*c"
pattern3 = "a+c"
pattern4 = "a?c"
pattern5 = "a{0,1}c"
pattern6 = "a[f-z]c"
pattern7 = "a[^f-z]c"
pattern8 = "a[^f-z]c|a{0,1}c"
pattern9 = "(ab){1,3}"
text = "abc aafb a$caaa!c ba3c aacxd abababcc baabaaca8c"

matches = re.findall(pattern9, text)
print(matches)

