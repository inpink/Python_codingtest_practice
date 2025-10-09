import sys
input = sys.stdin.readline

while True:
  data = list(map(int, input().split()))
  n = data[0]
  if n == 0:
    break

  heights = data[1:] # 나머지 n개의 수가 막대의 높이 리스트
  stack = []  # (start_index, height)
  max_area = 0 # 최대 직사각형 넓이 결과 변수

  # 히스토그램을 왼쪽부터 오른쪽으로 한 칸씩 탐색
  for i, height in enumerate(heights):
    start = i # 현재 막대의 시작 인덱스 (왼쪽으로 확장할 기준)

    # 스택의 top(stack[-1][1]) > 현재 막대 면, pop하면서 면적 계산
    # 즉, 스택에 담길때는 1 2 3 이런식으로 height가 높은게 무조건 더 위로 오는 구조
    while True:
      if len(stack)==0:
        break
      if stack[-1][1] <= height:
        break

      top_index, top_height = stack.pop()
      max_area = max(max_area, top_height * (i - top_index)) # 스택에 있는 지금까지의 top을 기준으로, 현재 i랑 height빼고 그전까지의 최대 면적 구함
      start = top_index  # 현재 막대는 pop한 막대의 시작점까지 확장 가능


    # ⭐스택이 비었거나(top이 없거나) top보다 현재 높이가 크면, 현재 (start,height)를 stack push한다.
    # 스택 비었으면 여기부터 계산해야 하니까 무조건 넣어야 한다.
    # 같은 높이라면 이미 더 왼쪽에서 시작한 막대가 있어서 굳이 push하지 않는다.
    # 예를 들어 [1, 1, 1]이면 첫 번째 (0,1)만 넣고 나머지는 skip해야 최대를 구할 수 있다.
    if len(stack) == 0 or stack[-1][1] < height:
      stack.append((start, height))

  # ⭐ 반복이 끝난 후 스택에 남은 막대 처리
  # 지금까진 new height보다 stack height가 작아지는 경우만 면적 계산해서 max_area에 반영했기 때문이다.
  # 기준은 맨 마지막인 n
  for top_index, top_height in stack:
    max_area = max(max_area, top_height * (n - top_index))

  print(max_area)

'''
- 스택을 이용한 풀이 
예)  7 2 1 4 5 1 3 3
초기 상태:
stack = []
max_area = 0

───────────────────────────────
i=0, height=2
stack 비어있음 → push (0,2)
stack = [(0,2)]

───────────────────────────────
i=1, height=1 (새로운 블럭 height가 top보다 더 낮으니 max_area 계산)
stack top (0,2) > 1 → pop (0,2)
  면적 = 2 * (1-0) = 2 → max_area = 2
  start = 0
push (0,1)
stack = [(0,1)]

───────────────────────────────
i=2, height=4
stack top (0,1) < 4 → push (2,4)
stack = [(0,1), (2,4)]

───────────────────────────────
i=3, height=5
stack top (2,4) < 5 → push (3,5)
stack = [(0,1), (2,4), (3,5)]

───────────────────────────────
i=4, height=1
stack top (3,5) > 1 → pop (3,5)
  면적 = 5 * (4-3) = 5
  start = 3
stack top (2,4) > 1 → pop (2,4)
  면적 = 4 * (4-2) = 8 → max_area = 8
  start = 2
stack top (0,1) ≤ 1 → stop
push (2,1)
stack = [(0,1), (2,1)]

───────────────────────────────
i=5, height=3
stack top (2,1) < 3 → push (5,3)
stack = [(0,1), (2,1), (5,3)]

───────────────────────────────
i=6, height=3
stack top (5,3) == 3 → push (6,3) 가능 (또는 skip)
stack = [(0,1), (2,1), (5,3), (6,3)]

───────────────────────────────
끝 (i=7, n=7) → 남은 스택 정리
pop (6,3): 면적 = 3 * (7-6) = 3
pop (5,3): 면적 = 3 * (7-5) = 6
pop (2,1): 면적 = 1 * (7-2) = 5
pop (0,1): 면적 = 1 * (7-0) = 7

최종 max_area = 8
───────────────────────────────
'''
