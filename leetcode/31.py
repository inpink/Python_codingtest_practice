class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    #1. 뒤에서부터 첫 감소 위치 찾기
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
      i -= 1

    #2. 감소한 숫자와 교환할 더 큰 숫자 찾기
    if i >= 0:
      j = len(nums) - 1
      while nums[j] <= nums[i]:
        j -= 1
      nums[i], nums[j] = nums[j], nums[i]

    #3. i 이후 숫자들을 뒤집기 (정렬)
    nums[i + 1:] = reversed(nums[i + 1:])

'''
새로운 배열 만들면 안되고 현재 배열에서 위치만 바뀌야 하는 문제

1,2,3이면 2<3이므로 1 3 2 되고, 3이후를 뒤집음 (그대로)
3,2,1이면 a<b인게없으므로 321되고 3이후를 뒤집음 (완전 뒤집혀서 123)

'''