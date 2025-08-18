import sys
input = sys.stdin.readline

r,c = map(int, input().split())
table = []
for i in range(r):
  table.append(list(input().strip()))

words = ["" for _ in range(c)]

for i in range(r):
  for j in range(c):
    words[j] += table[i][j]

count = 0

for i in range(r):
  # print(words)
  subStrings = set()

  for j in range(c):
    words[j] = words[j][1:]
    subStrings.add(words[j])

  if len(subStrings) == c:
    count += 1
  else:
    break

print(count)


