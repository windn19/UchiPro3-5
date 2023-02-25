import json


with open('example.json') as f:
    date = json.load(f)

total = 0
for it in date['clues']:
    total += it['value']

print(total)
