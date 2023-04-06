import re


pattern = r"[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text = "FERHAT.MOUSAVI@GMAIL.COM john.doe@example.com, jane_doe@example.co.uk, invalid-email@.com"

valid_emails = re.findall(pattern, text)
print(valid_emails)

pattern = r"\+?\d{0,2}\s?\(?\d{3,4}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}[-\s]?"
text = "05336659992, 0533 665 99 92, +90 533 665 99 92, 533 665 99 92, 533-665-99-92, (533)665-99-92"

phones = re.findall(pattern, text)
print(phones)
