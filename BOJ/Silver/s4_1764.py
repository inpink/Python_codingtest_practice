import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nl=set() #순서는 상관없고,중복도 없고,탐색이 있으니까 set 이용
ml=[]
for i in range(n):
    help=input().rstrip()
    nl.add(help)

for i in range(m):
    help=input().rstrip()
    if help in nl:
        ml.append(help)

ml=sorted(ml)
print(len(ml))
for i in ml:
    print(i)
