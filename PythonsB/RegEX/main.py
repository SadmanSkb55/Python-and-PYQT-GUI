import re

text = "Hello, my email is user@example.com. Please contact me!"

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

emails = re.findall(pattern, text)

for email in emails:
    print("Found email:", email)

text = """
Hello, my email is ahshit@example.com. 
Please contact me at okitaGG@example.co.uk 
or ohnofuck@example-domain.net.
"""

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

emails = re.findall(pattern, text)

print("Found email addresses:")
for email in emails:
    print(email)

