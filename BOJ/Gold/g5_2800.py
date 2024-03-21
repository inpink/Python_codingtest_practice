import sys
input=sys.stdin.readline

from itertools import product

s=input().rstrip()
listS=list(map(str,s))
length=len(s)
count=s.count("(")
brackets=[ ]

stack=[]
bracketCount=0
for i in range(length):
    if s[i]=="(":
        stack.append(i)
    elif s[i]==")":
        brackets.append([stack.pop(),i])
        
#print(brackets)

answers=set()
for p in product(range(2),repeat=count):
    #print(p)
    newS=list(listS)
    for i in range(len(p)):
        if p[i]==0:
            newS[brackets[i][0]]=''
            newS[brackets[i][1]]=''
            
    #print(newS)
    answers.add(''.join(newS))

answers=list(answers)
answers.remove(s)
answers.sort()
for i in answers:
    print(i)
