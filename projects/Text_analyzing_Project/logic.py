import re

Datafile = input("Enter text to analyze text and extract text:")
try:
    with open(Datafile, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{Datafile}' not found!")

text = re.sub(r'[^\w\s]', '', Datafile.lower())  # Keep only letters, numbers, spaces
text = re.sub(r'\s+', ' ', text).strip()     # Remove extra whitespace
print(text)

