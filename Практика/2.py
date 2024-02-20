string = 'Иванов Иван Иванович столкнулся с Петровым Петром Петровичем и за этим наблюдал Михайлов Михаил Михайлович'

import re

string = input()
pattern = r'[А-Я][а-я]+\s[А-Я][а-я]+\s[А-Я][а-я]+'
result = re.sub(pattern, 'Неизвестный', string)
print(result)