import re


pattern = r"^hello"
text = """HeLLo World!
hello world!
hEllo world!"""

matches = re.findall(pattern, text, flags=re.M | re.I)
print(matches)

pattern = r"hello.*world"
text = """hello.world hello
world hello\nworld hello world"""

matches = re.findall(pattern, text, flags=re.S)
print(matches)

pattern = r"""
    \b          # kelimenin başında olsun
    \d{1,3}     # ilk üç rakam
    (,\d{3})*
    \b          # kelimenin sonunda olsun
    """
text = """
Ali: 234,789 TL
Hasan: 345,980 TL
Mahmut: 12,000,000 TL
Semih: 1,655,000 TL
Merve: 345,765,120 TL
"""

matches = re.finditer(pattern, text, flags=re.X)
for match in matches:
    print(match.group())
