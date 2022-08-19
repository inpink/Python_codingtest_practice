import sys
input = sys.stdin.readline


n=int(input())
l=list(map(int,input().split()))
sum=[l[0]] #비어있는 채로 최대값 나오지 않게 하기 위해
for i in range(n-1): #n=10이면, i=0~8
    #언제 연속합이 끊기는 지를 생각해 봐야 한다.
    #연속합을 했을 때보다, 단일 수가 더 크면 끊겨야 한다.
    #안끊기면 sum[i]에 지금까지의 합이 다 담기는 것이고, 끊기면 sum[i]가 단일 수로 업데이트 되므로 연속합을 구하는 것이 맞다.
    sum.append(max(sum[i]+l[i+1],l[i+1]))

print(max(sum))
