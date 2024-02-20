import re


pattern = r'[\w\.-]+@[\w\.-]+\w+'
pat = re.compile(r"[\w\.-]+@([\w-]+\.?){2,}")
string = """ Обратная связь: onlineshop@gmail.com,
vasya-shop@yandex.ru. Для сотрудничества:
ad.online_shop@gmail.com!
"""

emails = re.findall(pattern, string)
for emails in emails:
    print(emails)
