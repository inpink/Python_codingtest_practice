import sys
input = sys.stdin.readline

while True:
	a=int(input())
	if a==0:
		break
	a=str(a)
	ist="yes"
	for i in range(len(a)//2):
		if a[i]!=a[-1*(i+1)]:
			ist="no"
			break
	print(ist)

#회문, 펠린드롬 수