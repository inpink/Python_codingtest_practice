
def maxArea(self, height):
  #투 포인터 초기화
  left = 0
  right = len(height) - 1
  max_area = 0

  #포인터가 서로 만나기 전까지 반복
  while left < right:
    #현재 높이와 너비를 계산
    current_height = min(height[left], height[right])
    current_width = right - left
    current_area = current_height * current_width

    #최대 면적 업데이트
    max_area = max(max_area, current_area)

    #낮은 쪽 포인터를 이동
    if height[left] < height[right]:
      left += 1
    else:
      right -= 1

  return max_area

'''
⭐️ 왜 낮은 쪽 포인터를 이동시키는가?
: 낮은 쪽 포인터를 이동시켜야만 높이를 증가시킬 가능성이 생깁니다.
: 높은 쪽 포인터를 이동해봐야 높이에는 아무 영향을 주지 못합니다. (현재 컨테이너의 높이는 더 낮은 쪽에 의해 결정되기 때문입니다.)


'''