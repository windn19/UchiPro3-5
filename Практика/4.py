import re
import sys


pattern = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
for line in sys.stdin:
    string = line.strip()
    if re.match(pattern, string):
        print(True)
    else:
        print(False)
