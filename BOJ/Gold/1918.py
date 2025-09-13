import sys
input = sys.stdin.readline

s=input().rstrip()

stack=[]
ans=""
for c in s:
  if c.isalpha():
    ans+=c
  else:
    if c=="(":
      stack.append(c)
    elif c=="+" or c=="-":
      while True:
        if len(stack)==0:
          break
        if stack[-1]=="(":
          break
        ans+=stack.pop()
      stack.append(c)
    elif c=="*" or c=="/":
      while True:
        if len(stack)==0:
          break
        if stack[-1]!="*" and stack[-1]!="/":
          break
        ans+=stack.pop()
      stack.append(c)
    elif c==")":
      while True:
        if len(stack)==0:
          break
        if stack[-1]=="(":
          stack.pop()
          break
        ans+=stack.pop()
  print(c, ans, stack)

while True:
  if len(stack)==0:
    break
  ans+=stack.pop()

print(ans)

