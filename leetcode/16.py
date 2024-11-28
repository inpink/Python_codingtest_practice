def threeSumClosest(nums, target):
  nums.sort()
  closest_sum = float(
    'inf')  # 초기값으로 무한대 설정 (nums[-1] + nums[-2] + nums[-3]도 가능)

  for i in range(len(nums) - 2):
    left, right = i + 1, len(nums) - 1  # 투 포인터

    while left < right:
      current_sum = nums[i] + nums[left] + nums[right]

      # 더 가까운 합을 찾으면 업데이트
      if abs(target - current_sum) < abs(target - closest_sum):
        closest_sum = current_sum

      # target과 비교해 포인터 이동
      if current_sum < target:
        left += 1
      elif current_sum > target:
        right -= 1
      else:  # current_sum이 정확히 target과 같다면 바로 반환
        return current_sum

  return closest_sum


'''
마찬가지로 투 포인터 문제
마찬가지로 처음 값 고정하고 나머지 두 값 찾는 방식
"더 가까운 합을 찾으면 업데이트"
'''
