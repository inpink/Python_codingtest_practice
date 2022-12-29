import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
Glist = []
for i in range(m):
    a, b, c = map(int, input().split())
    Glist.append([c, a, b])

Glist.sort()


def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]


Vroot = [i for i in range(n + 1)]
ans = 0
for w, a, b in Glist:
    aRoot = find(a)
    bRoot = find(b)

    if aRoot != bRoot:
        Vroot[bRoot] = aRoot
        ans += w
    # print(Vroot)
print(ans)

