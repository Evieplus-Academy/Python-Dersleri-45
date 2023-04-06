import re


pattern = "fda."
text = """abc xyz ABC 345 abc fda
abc jhg 456
abc 890 ujk fda"""

# matches = re.findall(pattern, text, flags=re.IGNORECASE)
# matches = re.findall(pattern, text, flags=re.MULTILINE)
matches = re.findall(pattern, text, flags=re.DOTALL)
print(matches)


pattern = r"""
        \b          # Kelimenin başında olsun
        \d{1,3}
        (,\d{3})*
        \b
"""

text = "Benim 300,000,000 TL param var. Hasanın 25,000 TL si var."

matches = re.finditer(pattern, text, flags=re.VERBOSE)
for match in matches:
    print(match.group())
