import sys

input = sys.stdin.readline

v, e = map(int, input().split())
Glist = []
for i in range(e):
    a, b, c = map(int, input().split())
    Glist.append([c, a, b])

Glist.sort()


def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]


Vroot = [i for i in range(v + 1)]
ans = 0
last_w = 0
for w, a, b in Glist:
    aRoot = find(a)
    bRoot = find(b)

    if aRoot != bRoot:
        Vroot[bRoot] = aRoot
        ans += w
        last_w = w
        # print(a,b)
    # print(Vroot)
print(ans - last_w)
