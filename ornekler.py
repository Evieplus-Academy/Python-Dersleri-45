import re


pattern = r"[a-zA-Z0-9._]+@[a-zA-Z0-9-.]+\.[a-zA-Z]{2,}"
text = "ferhat.mousavi@gmail.com ezgi_OZGUR@gmail.COM Serkan.Bayram@.com john.carter1998@google.co.uk hasan.bayrakli@mail.company.com.tr"

matches = re.findall(pattern, text)
print(matches)


pattern = r"\b\d{2}[.-]\d{2}[.-]\d{4}\b"
text = "Bugün 09.04.2023. Yarın 10-04-2023."

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())

pattern = r"\(?\d{3}[)-]-?\d{3}-?\d{2}-?\d{2}"
phone_pattern = re.compile(pattern)
text = "555-4327645, 533-543-88-22, (533)6659992, (543)-876-99-92, 5425424242"

matches = phone_pattern.findall(text)
print(matches)
