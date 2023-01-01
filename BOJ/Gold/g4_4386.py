import sys

input = sys.stdin.readline

n = int(input())
tmp = []

for i in range(n):
    x, y = map(float, input().split())
    tmp.append([x, y])  # 임시로 x,y좌표만 담아둠

# 간선은 1+2+...+n-1개 생김
Glist = []
for i in range(n - 1):
    a = tmp[i]
    for j in range(i + 1, n):  # 중첩for문으로, n개의 별을 잇는 모든 간선의 가중치를 구하고, ★각 (x,y)별자리를 정점 1개로 보고, 정점 번호 index를 배분함.
        # 각 점의 고유 번호(index)로 i,j를 부여하여 w,a,b를 맞춤. 정점은 n개이므로, 고유 번호는 0~n-1번까지 분배됨. 간선 개수가 1+2+...+n-1개인거고, 정점 개수는 n개.
        b = tmp[j]
        Glist.append([((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5, i, j])  # 거리는 간단히 유클라디안

Glist.sort()


def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]


Vroot = [i for i in range(n)]  # 고유번호를 0번부터 배정하였으므로 0~n-1번까지 정점 있음
ans = 0
for w, a, b in Glist:
    aRoot = find(a)
    bRoot = find(b)

    if aRoot != bRoot:
        Vroot[bRoot] = aRoot
        ans += w
        # print(a,b)
    # print(Vroot)
print(round(ans, 2))  # 2자리까지 반올림하여 출력하면 됨
