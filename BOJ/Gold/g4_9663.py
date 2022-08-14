n = int(input())

chk=[0]*n #세로 열에 들어 왔는가
chk2=[0]*(n*2) #좌->우측 대각선
chk3=[0]*(n*2) #우->좌측 대각선

ans=0
s=[]

def dfs(x):
    global ans
    if (x==n): #n개 다 채워지면
        ans+=1
        print(s)
        return

    for i in range(n): #i=0,1,2,3,4...n
        if chk[i] or chk2[i+x] or chk3[i-x + n-1]: #셋 중 하나라도 True이면 걸림
            continue
        chk[i]=1
        chk2[i+x]=1
        chk3[i-x + n-1]=1
        s.append([x,i])
        dfs(x+1) #x+1을 넣어주기 때문에, 하나의 s에서 하나의 x에서는 딱 하나의 값만 가지게 되는 것이다.
        chk[i]=0
        chk2[i+x]=0
        chk3[i+(n-x)-1]=0
        s.pop()



dfs(0)
print(ans)

