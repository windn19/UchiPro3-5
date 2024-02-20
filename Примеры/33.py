import re

pattern = r'\d\d\.\d\d'
string = '01.12 должно было произойти что-то, но произойдет 02.12.2023'

match = re.findall(pattern, string)
print(match)  # ['01.12', '02.12']

result = re.split(pattern, string)
print(result)  # ['', ' должно было произойти что-то, но произойдет ', '.2023']

new_string = re.sub(pattern, '-удалено-', string)
print(new_string)  # -удалено- должно было произойти что-то, но произойдет -удалено-.2023
