class Solution:
  def search(self, nums: List[int], target: int) -> int:
    leng=len(nums)
    start = 0
    end = leng-1

    if leng==1:
      if nums[0]==target:
        return 0
      else:
        return -1

    while True:
      if start>end:
        break

      mid = (start + end) //2
      print(start,end,mid)

      if nums[start] == target:
        return start
      elif nums[end] == target:
        return end
      elif nums[mid] == target:
        return mid

      if nums[start] < nums[mid] and nums[mid] < nums[end]:
        if nums[mid] < target:
          start=mid +1
        else:
          end=mid -1
      elif nums[start] < nums[mid] and nums[mid] > nums[start]:
        if nums[start] < target < nums[mid] :
          end = mid -1
        else:
          start=mid +1
      elif nums[start] > nums[mid] and nums[mid] < nums[start]:
        if nums[mid] < target< nums[end]:
          start =mid+1
        else:
          end=mid - 1
      else:
        break

    return -1



'''


 if start>end:  ⭐
        break

⭐⭐⭐ 우리가 쓰는 이분탐색 구현 코드 에서 len==1일 때는 예외로 둬야 한다!!!! 대부분이 문제에서 n>=2이긴 하지만 아닐 때는 꼭 예외처리해야함 ⭐⭐⭐ 
⭐if문이 elif까지만 있고 else가 없다면 예상한대로 동작하지 않을 수 있다. ⭐⭐start==end 경우 때문에 이분탐색에서 else는 반드시 있어야 한다 ⭐⭐

'''