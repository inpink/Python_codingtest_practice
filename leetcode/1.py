def twoSum(nums, target):
  map=dict()
  for i in range(len(nums)):
    num=nums[i]
    if num in map:
      map[num].append(i)
    else:
      map[num]=[i]
  print(map)

  for num in nums:
    need = target - num
    if need in map:
      if num==need:
        if len(map[num])>=2:
          return [map[num][0],map[num][1]]
      else:
        return [map[num][0],map[need][0]]




print(twoSum([5,2,7,11,15],9)) #1,2   #2 5 7 11 15
print(twoSum([5,2,7,11,15],22)) #1,2   #2 5 7 11 15
print(twoSum([3,3],6)) #0,1


'''
정수 배열 nums와 정수 target이 주어졌을 때, 두 수를 더하여 target이 되는 두 숫자의 인덱스를 반환하세요.

각 입력에 대해 정답이 반드시 하나 존재한다고 가정할 수 있으며, 같은 요소를 두 번 사용할 수는 없습니다.

정답은 순서에 상관없이 반환해도 됩니다.


조건)
nums 길이가 2~10^4
nums[i]는 -10^9 ~ 10^9
target도 -10^9 ~ 10^9
Follow-up: O(n^2)보다 작게 가능?

예)
nums = [2,7,11,15], target = 9
0,1

brute force로하면 10^4*10^4정도로가능하긴함 
그래도 더작은 시간복잡도를 원한다면
전체 정렬함=> nlogn
'''