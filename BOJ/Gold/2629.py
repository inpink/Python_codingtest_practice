import sys
input = sys.stdin.readline

weight_count=int(input())
weights=list(map(int,input().split()))
bead_count=int(input())
beads=list(map(int,input().split()))

possibles=set()
possibles.add(weights[0])
for i in range(1, weight_count):
  new_possible=set()
  this_weight=weights[i]
  new_possible.add(this_weight)

  for x in possibles:
    new_possible.add(abs(this_weight-x))
    new_possible.add(this_weight+x)
  possibles.update(new_possible)
# print(possibles)

for bead in beads:
  if bead in possibles:
    print('Y', end=' ')
  else:
    print('N', end=' ')