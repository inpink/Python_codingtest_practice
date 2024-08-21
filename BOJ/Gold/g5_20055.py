import sys
input = sys.stdin.readline

def isEnd(belt,k):
  return aList.count(0)>=k

def rotate(belt):
  belt=list(belt)
  newBelt= list([belt[-1]]+belt[0:n*2-1])
  newBelt= downIfPossible(newBelt)
  return newBelt

def downIfPossible(belt):
  belt=list(belt)
  if belt[n-1][1]!=-1:
    thisRobotNumber=belt[n-1][1]
    del robotsOrder[thisRobotNumber]
    belt[n-1][1]=-1 # 내리기

  return belt

def findBeltIndexByNumber(belt,findNumber):
  for i in range(len(belt)):
    number,robot=belt[i]
    if number==findNumber:
      return i

def moveRobot(belt):
  belt=list(belt)
  for robotNumber in robotsOrder: #먼저 올린 로봇 순서대
    nodeNumber=robotsOrder[robotNumber]
    beltIndex=findBeltIndexByNumber(belt,nodeNumber)

    number, robot = belt[beltIndex]
    if robot!=-1:
      nextNumber, nextRobot = belt[(beltIndex+1)%len(belt)]
      if (aList[nextNumber]>=1 and nextRobot==-1): #로봇이동가능
        belt[beltIndex][1]=-1
        robotsOrder[robot]=nextNumber
        belt[(beltIndex+1)%len(belt)][1]=robot
        aList[nextNumber]-=1

  belt = downIfPossible(belt)
  return belt

def upRobotIfPossible(belt):
  global robotCount
  belt=list(belt)
  number, robot = belt[0]


  if aList[number]>=1 and robot==-1: #로봇올릴 수 있음
    robotCount+=1
    nextRobotNumber=robotCount

    belt[0][1]= nextRobotNumber #로봇번호
    aList[number]-=1
    robotsOrder[nextRobotNumber]=number #nextRobotNumber번째 삽입된 로의 노드 번호는 number입니다.

  return belt

n,k=map(int,input().split())
aList=[-1]+list(map(int,input().split())) #내구성 리스트


belt=[] #[number,robot]
robotsOrder=dict() #belt에서 몇번째 index에 있는지
robotCount=0

for i in range(1,n*2+1):
  belt.append([i,-1])
#print(belt)

#print(rotate(belt))

round=1
while True:
  #print("round",round)
  #1벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
  belt = rotate(belt)
  #print("1",belt)

  #2가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
  belt = moveRobot(belt)
  #print("2",belt,"aLIst",aList)

  #3올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
  belt= upRobotIfPossible(belt)
  #print(3,belt,"robotsOrer",robotsOrder,"aLIst",aList)

  #4내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
  if isEnd(belt,k):
    print(round)
    exit(0)
  #print(4,belt)

  round+=1

'''
1 2 3
6 5 4

number_robot
5_b 6 1_a
4 3 2

0번째: 넣는곳
n-1번쨰: 빼는곳
10:50~
1...N ->
<- 2N 2N-1 ... N+1

맨처음
1: 올리는 위치(여기에만 로봇 올릴 수 있음)
N: 내리는 위치(여기온 로봇은 항상 내림)

로봇은 벨트 위에서 스스로 이동할 수 있다

그 칸의 내구도 1 감소: 로봇을 올리는 위치에 올리거나 / 로봇이 어떤 칸으로 이동하면

순서대로 이게 일어남
1. 벨트가 한 칸 회전한다. 그 위에있는 로봇도 같이 움직임.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
 이동 가능 조건: 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있다
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번부터 반복한다.

출력: 종료되었을 때 몇 번째 단계가 진행 중이었는지
(처음은 1단계)

2 ≤ N ≤ 100
1 ≤ K ≤ 2N
1 ≤ Ai ≤ 1,000

칸이 총 2N개
처음 i번 칸의 내구도는 Ai
2N번은 1번으로 이동함

예제 1
n=3 k=2
1 2 1 2 1 2

내구도가 0인 칸이 2개 이상이면 종료하고 2 번째단계가 진행되었다
1 2 3
6 5 4

6_a 1 2
5 4 3

1 2 1 2 1 1

---

5 6_a 1
4 3 2

5_b 6 1_a
4 3 2

0 2 1 2 0 1
=> 종료 2단계


예제 2
n=3 k=6
10 10 10 10 10 10

1 2 3
6 5 4
내구도가 0인 칸이 5개 이상이면 종료하고 31 번째단계가 진행되었다



'''