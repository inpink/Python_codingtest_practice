import sys
input = sys.stdin.readline

h, w = map(int, input().split())

heights = list(map(int, input().split()))

maxHeight = heights[0]
maxPosition = 0
accumHeight = 0

rains = 0
for i in range(1, w - 1):
    curHeight = heights[i]
    beforeHeight = heights[i - 1]
    nextHeight = heights[i + 1]
    # print(beforeHeight,curHeight,nextHeight)

    leftMaxHeight = max(heights[:i])
    rightMaxHeight = max(heights[i:])

    if curHeight < leftMaxHeight and curHeight < rightMaxHeight:
        minLeftRightHeight = min(leftMaxHeight, rightMaxHeight)

        rains += (minLeftRightHeight - curHeight)

print(rains)

'''
index가 a인 지점에서 빗물이 고이려면, 전체 height에서 a왼쪽에 있는 가장 큰 값과 a오른쪽에 있는 가장 큰 값보다 a가 작아야 한다.
예를 들어서 index가 5인 a가 1일 때, index가 3인 height가 3이고 index가 7인 height가 6이면,  3 1 6으로 둘러쌓인 것으로 빗물이 쌓이게 된다.
이 때, 쌓이는 빗물 양은 min(leftMaxHeight, rightMaxHeight) - a의 height = 2이다.
이 과정을 모든 height에 대해 검사하면 된다.

시간복잡도는 w:500, h:500까지에서, "left & right의 max를 검사하는 과정이 매번 500번(width) * 모든 index지점에 대해 검사하는 500번 = 250,000"으로 시간복잡도 내에 통과한다.  
'''
