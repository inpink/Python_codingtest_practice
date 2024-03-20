import sys
input=sys.stdin.readline

#dp
#감소하는수 0 1
#0~100만번째 감소하는 수 구하기
n=int(input())
if n>=1023:
    print(-1)
    exit(0)
    
nums=[]

#초기값 설정
beforeDic={}
for i in range(10):
    beforeDic[i]=[i]
    nums.append(i)
print(beforeDic)
for i in range(2,10+1): #i=2일 때 2자리 수 결정
    tmpDic={}
    for a in range(1,10):
        tmpDic[a]=[]
        
    for j in range(i-1,9+1): #i=3일 때 2부터 시작, i=4일 때 3부터 시작, i=10일때 9부터 시작 모두 9까지
        for k in range(0,j): #j=4일 때 0부터 3까지 (0은 없을때도 있음)
            if k not in beforeDic:
                continue
            for p in beforeDic[k]:
                nextNum=str(j)+str(p)
                nums.append(nextNum)
                tmpDic[j].append(nextNum)
    beforeDic=tmpDic
print(int(nums[n]))
