import sys
input = sys.stdin.readline

k=int(input()) #1m^2당 자라는 참외의 개수
'''
최대 가로변, 최대 세로변과 붙어있는 변을 구하기만 하면 쉽게 풀리는 문제.
붙어있는 변은, 가로or세로임이 확실해진 상태에서(l[i][0]==1 or 2등 )
리스트에서 +1번째와 -1번째이다. 인덱스 에러(리스트 범위 초과)를 막기 위해 +1번째 -1번째 구할 때 %쓰는 것 잊지말기!
'''
l=[]
max_w = 0 #최대 가로
max_h = 0 #최대 세로

for i in range(6): #6번 반복하여 입력받는다.
    a, b = map(int, input().split())
    l.append([a,b])
    if a==1 or a==2: #동,서일때
        if b>=max_w: #최대 가로 구해주기
            max_w=b
    else: #남,북일 때
        if b>=max_h: #최대 세로 구해주기
            max_h=b

h_1 = 0#최대 가로랑 붙어있는 세로변( 최대 세로에서 빼줄 것)
w_1 = 0#최대 세로랑 붙어있는 가로변 ( 최대 가로에서 빼줄 것)
for i in range(len(l)):
    if (l[i][0]==1 or l[i][0]==2 ) and l[i][1]==max_w: #최대 가로를 발견하면
        h_1=min(l[(i-1)%6][1], l[(i+1)%6][1])
    elif (l[i][0]==3 or l[i][0]==4 ) and l[i][1]==max_h: #최대 세로를 발견하면
        w_1=min(l[(i-1)%6][1], l[(i+1)%6][1])

#print(l,max_w,max_h,h_1,w_1)


whole=max_w*max_h #큰 사각형의 넓이
part=(max_h-h_1) * (max_w-w_1)
print(k*(whole-part))
