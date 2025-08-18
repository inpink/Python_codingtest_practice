import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

t=int(input())


def dfs(thisStudent, nextStudent, numbers, dp):
  print(thisStudent, nextStudent, dp)
  if dp[thisStudent]==nextStudent: #자기 자신 사이클 만남
    return thisStudent

  dp[thisStudent]=thisStudent

  parent = dfs(numbers[thisStudent], numbers[numbers[thisStudent]], numbers, dp)
  print("backup",parent,thisStudent,nextStudent,dp)



for i in range(t):
  n=int(input())
  numbers=[0] +x

  dp = [ 0 for i in range(n+1)]

  for j in range(1,n+1):

    dfs(j, numbers[j], numbers,dp)

