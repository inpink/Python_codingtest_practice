import sys
input=sys.stdin.readline


def toCountMap(s):
  m=dict()
  for i in s:
    if i in m:
      m[i]+=1
    else:
      m[i]=1
  return m

def isContainOdd(m):
  for count in m.values():
    if count%2!=0:
      return True
  return False

def isOnlyOneOdd(m):
  oddCount=0
  for count in m.values():
    if count%2!=0:
      oddCount+=1

  if oddCount!=1:
    return False
  else:
    return True

def findUnique(m):
  unique=[]
  for key in m:
    value=m[key]
    for i in range(value//2):
      unique.append(key)

  return sorted(unique)

s=input().strip()
length=len(s)
ans=['' for i in range(length)]

m=toCountMap(s)

if length%2==0:
  if isContainOdd(m):
    print("I'm Sorry Hansoo")
    exit(0)

  unique=findUnique(m)

  half=''.join(unique)
  print(half+half[::-1])
  exit(0)


else: #홀수일 때
  if not isOnlyOneOdd(m):
    print("I'm Sorry Hansoo")
    exit(0)

  for key in m:
    value=m[key]
    if value%2!=0:
      center=key
      m[key]-=1

  unique=findUnique(m)

  half=''.join(unique)
  print(half+center+half[::-1])
  exit(0)



'''
8:53~

임한수의 영어 이름(입력, 알파벳 대문자로만 된 최대 50글자)으로 팰린드롬을 만들려고 하는데
임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

50!은 당연히 시간초과 (브루투포스 X)

만약 불가능할 때는 "I'm Sorry Hansoo"를 출력
=> 길이가 짝수 / 홀수
길이가 홀수일 때, 중앙에는 개수가 홀수개수인 것만 올 수 있음.
따라서 길이가 홀수일 때, 홀수 개수인 것이 없으면 만들 수 없음.
길이가 홀수일 때, 홀수 개인 것 중 가장 느린 것 1개를 중앙에 배치함. 나머지들은 빠른 순서대로 배치함.
 만약 홀수 개수인 게 2개 이상 있으면 펠린드롬 불가 

길이가 짝수일 때, 홀수 개수인 것이 있으면 펠린드롬 만들 수 없음.
길이가 짝수일때, 반 나눠서 알파벳 빠른 것들을 앞쪽에 배치하면됨

정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력

예제 1
AABB
A:2 B:2 길이 4
A__A
ABBA

예제 2
AAABB
A:3 B:2 길이 5
__A__
A_A_A
ABABA

예제 3
ABACABA
A:4, B:2, C:1 길이 7
___C___
AA_C_AA
AABCBAA

예제 4
ABCD
A:1, B:1, C:1, D:1
홀수짝이 1개 초과라 불가
'''