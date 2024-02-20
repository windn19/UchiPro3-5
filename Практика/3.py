import re

pattern = r'кот.*кот'
for i in range(int(input())):
    string = input()
    if re.search(pattern, string):
        print(string)
