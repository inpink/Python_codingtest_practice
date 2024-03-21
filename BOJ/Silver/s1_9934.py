import sys
input=sys.stdin.readline

#재귀, 분할 정복

def rec(depth,start,end):
    #print(depth,start,end)
    length=end-start
    if length==3:
        ans[depth].append(numbers[start+1]) #분할의 root
        ans[depth+1].append(numbers[start]) #분할의 left
        ans[depth+1].append(numbers[start+2]) #분할의 right
        return

    #분할이 필요한 경우
    mid=(start+end)//2
    ans[depth].append(numbers[mid])
    rec(depth+1,start,mid) #왼쪽 분할
    rec(depth+1,mid+1,end) #오른쪽 분할

k=int(input())
numbers=list(map(int,input().split()))
length=len(numbers)
ans=[[]for i in range(k)]
rec(0,0,length)

for i in ans:
    print(*i)
'''
깊이는 k
맨 중앙에 있는 값이 root
총 길이는 2^k-1

남은것 중에서도 맨 중앙에 있는 것이 남은것중의 root
남은것이 3개이면 말단left,root,말단right 결정됨

분할된 횟수만큼 담아주면 됨

'''
