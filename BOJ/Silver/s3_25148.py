'''import sys

input = sys.stdin.readline

# 7 77
a, k = map(int, input().split())

l = []
while True:
    if k <= a:
        break
    l.append(k)
    k = k // 2

# print(l)

count = 0
for i in range(1, len(l) + 1):  # 4개면 i= 1,2,3,4    1개면 i=1   3개면 i=1,2,3
    while True:
        # print(i,a)
        if a == l[i * -1]:
            break

        if a * 2 <= l[i * -1]:  # 가능하면 2배
            count += 1
            a *= 2
        else:  # 2배로 바로 안되면 +1
            count += 1
            a += 1
print(count)

위는, 거쳐야 하는 지점을 미리 l에 담아 두고 a에서부터 k로 가는 방식
'''

#이 방법은, l을 미리 만들지 않고 K에서부터 A로 가는 방식