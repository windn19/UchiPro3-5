import re

pattern1 = r'\d\d\.\d\d'
pattern2 = r'\d\d\.\d\d\.\d{4}'
string = '01.12 должно было произойти что-то, но произойдет 02.12.2023'

match1 = re.search(pattern1, string)
match2 = re.search(pattern2, string)
print(match1)  # <re.Match object; span=(0, 5), match='01.12'>
print(match2)  # <re.Match object; span=(50, 60), match='02.12.2023'>

match3 = re.match(pattern1, string)
match4 = re.match(pattern2, string)
print(match3)  # <re.Match object; span=(0, 5), match='01.12'>
print(match4)  # None
