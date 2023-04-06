import re

pattern1 = r"(\d\d\d)*a"
pattern2 = r"(\d\D\D){1,3}"
pattern3 = r"(\w\w\w){1,3}"
pattern4 = r"(\W\W){1,3}"
pattern5 = r"(\s\s){1,3}"
pattern6 = r"(\S\S){1,3}"
text = "1234\t 4567*!@7890a 0124_  _acas"

pattern = r"hello\s+\w+"
text = "hello world hello   python hello\nferhat"

matches = re.findall(pattern, text)
print(matches)
