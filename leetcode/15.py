def three_sum(nums):
  nums.sort()  #배열을 정렬하여 투 포인터 접근법을 용이하게 만듦
  result = []
  n = len(nums)

  for i in range(n):
    #첫 번째 숫자에 대해 중복된 요소 건너뛰기
    if i > 0 and nums[i] == nums[i - 1]:
      continue

    #투 포인터
    left, right = i + 1, n - 1
    while left < right:
      total = nums[i] + nums[left] + nums[right]
      if total == 0:
        result.append([nums[i], nums[left], nums[right]])

        #두 번째와 세 번째 숫자에 대해 중복된 요소 건너뛰기
        while left < right and nums[left] == nums[left + 1]:
          left += 1
        while left < right and nums[right] == nums[right - 1]:
          right -= 1

        #포인터 이동
        left += 1
        right -= 1
      elif total < 0:
        left += 1  #합을 늘림
      else:
        right -= 1  #합을 줄임

  return result


'''
배열에서 합이 0이 되는 모든 고유한 3개의 숫자 조합(트리플릿)을 찾는 문제

투 포인터로 해결. (3000^3은 시간초과인데 3000^2은 가능)
a번째 숫자 고정하고 맞는 b,c번째 찾는 방식. 
이 때, 이 문제의 핵심은 """중복된 트리플릿이 없어야 함"""
=> 따라서 중복을 제거하는 작업이 필요함. 정렬을 했기에, 중복된 숫자는 계속 건너띄면 ""고유한 셋이 나옴""   


    
'''