import sys
input=sys.stdin.readline

n=int(input())
numbers=list(map(int,input().split()))

counts={}
for number in numbers:
    if number in counts:
        counts[number]+=1
    else:
        counts[number]=1

#print(counts)

uniqueNumbers=set(numbers)
ans=0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i==j:
            continue
        #print(i,j)

        mine=numbers[i]
        other1=numbers[j]
        # 잠시 자신 것, 후보군 뺴놓기
        counts[mine]-=1
        counts[other1]-=1

        need=mine-other1

        if need in counts and counts[need]>0:
            ans+=1
            #print(mine,other1)
            # 뺀 거 다시 돌려놓기
            counts[mine]+=1
            counts[other1]+=1
            break

        # 뺀 거 다시 돌려놓기
        counts[mine]+=1
        counts[other1]+=1

print(ans)
