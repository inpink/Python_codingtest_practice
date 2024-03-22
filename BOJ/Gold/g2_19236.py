import sys
input=sys.stdin.readline

import copy

#↑, ↖, ←, ↙, ↓, ↘, →, ↗
directions=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

graph=[[] for i in range(4)]
positions= {}
for i in range(4):
    row=list(map(int,input().split()))
    for j in range(4):
        graph[i].append([row[j*2],row[j*2+1]-1])
        positions[row[j*2]]=[i,j]

firstEatenFish=graph[0][0][0]
graph[0][0][0]='shark'
score=firstEatenFish
del positions[firstEatenFish]
positions['shark']=[0,0] #x,y
'''
for i in graph:
    print(i)
print(positions)
'''

def moveFishes(graph,positions):
    for i in range(1,16+1):
        if i not in positions:
            continue
        x,y=positions[i]
        curFish,curDirection=graph[x][y]
        while True:
            #print(graph,i,curFish,curDirection)
            xDir,yDir=directions[curDirection]
            nextX,nextY=x+xDir,y+yDir
            if 0<=nextX<=3 and 0<=nextY<=3:
                nextFish,nextDirection=graph[nextX][nextY]
                if nextFish!='shark':
                    graph[x][y]=[nextFish,nextDirection]
                    graph[nextX][nextY]=[curFish,curDirection]
                    positions[i]=[nextX,nextY]
                    if str(nextFish).isdigit():
                        positions[nextFish]=[x,y]
                    break

            curDirection=(curDirection+1)%8

    '''
    for i in graph:
        print(i)
    print(positions)
    '''

def dfs(score, graph, positions):
    global maxScore
    maxScore=max(maxScore,score)
    #print("dfs:",graph,positions)
    moveFishes(graph,positions)
    sharkX,sharkY=positions['shark']
    sharkDir=graph[sharkX][sharkY][1]
    sharkDirX,sharkDirY=directions[sharkDir]

    isPossible=False
    for i in range(3): #최대 3번
        nextX,nextY=sharkX+sharkDirX*(i+1), sharkY+sharkDirY*(i+1)
        if nextX<0 or nextX>=4 or nextY<0 or nextY>=4:
            break
        nextFish,nextDir=graph[nextX][nextY]
        if str(nextFish).isdigit():
            graph[sharkX][sharkY]=['','']
            graph[nextX][nextY]=['shark',nextDir]
            positions['shark']=[nextX,nextY]
            del positions[nextFish]
            #print("nextFish:",nextFish)

            dfs(score + nextFish,copy.deepcopy(graph),copy.deepcopy(positions))

            graph[sharkX][sharkY]=['shark',sharkDir]
            graph[nextX][nextY]=[nextFish,nextDir]
            positions['shark']=[sharkX,sharkY]
            positions[nextFish]=[nextX,nextY]


maxScore=0
dfs(score,graph,positions)
print(maxScore)