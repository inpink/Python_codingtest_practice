def four_sum(nums, target):
  nums.sort()
  n = len(nums)
  result = []

  for i in range(n):
    if i > 0 and nums[i] == nums[i - 1]:  #중복 처리
      continue
    for j in range(i + 1, n):
      if j > i + 1 and nums[j] == nums[j - 1]:  #중복 처리
        continue
      left, right = j + 1, n - 1  #투 포인터
      while left < right:
        total = nums[i] + nums[j] + nums[left] + nums[right]
        if total == target:
          result.append([nums[i], nums[j], nums[left], nums[right]])
          left += 1
          right -= 1
          # 중복 처리
          while left < right and nums[left] == nums[left - 1]:
            left += 1
          while left < right and nums[right] == nums[right + 1]:
            right -= 1
        elif total < target:
          left += 1
        else:
          right -= 1

  return result

'''
앞전에 풀었던 xsum 문제들과 유사

4개 숫자 찾아야하니까
a,b 정해놓고 나머지 c,d는 투포인터로 찾는 것
이걸 모든 a,b 경우의 수에 대해 반복
'''