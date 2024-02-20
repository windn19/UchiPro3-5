import re

pattern = r'[-_\.\,!*\s]+'

string = input()
print(*re.split(pattern, string), sep='\n')
