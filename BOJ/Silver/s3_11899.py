s=input()

stack = []

ans=0
for i in range(len(s)):
  if s[i]==')':
    if len(stack)>0 and stack[-1]=='(':
      stack.pop()
    else:
      ans+=1

  elif s[i]=='(':
    stack.append(s[i])

if len(stack)!=0:
  ans+=len(stack)

print(ans)

'''
가능한 한 괄호열을 적게 추가
S길이 1~50
'''