import sys

input = sys.stdin.readline

from datetime import datetime

y = str(datetime.today().year)
m = str(datetime.today().month)
d = str(datetime.today().day)

leny = len(y)
if len(y) <= 3:  # 1,2,3자리 수면
    help = y
    y = ''
    for i in range(4 - leny):  # 부족한 0 개수만큼
        y += '0'
    y += help

if len(m) == 1:  # 한자리 수면
    m = '0' + m

if len(d) == 1:  # 한 자리 수면
    d = '0' + d
print(y + '-' + m + '-' + d)