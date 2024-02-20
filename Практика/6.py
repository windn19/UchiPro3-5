import re

text = input()

text = re.sub(r'\s{2,}', ' ', text)
text = re.sub(r'\s+(\W)', r'\1', text)
print(text)