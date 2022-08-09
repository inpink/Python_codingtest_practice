import sys

input = sys.stdin.readline
'''
배열 A의 subsequence를 잡아 이들의 mex 값을 배열 $B$의 맨 뒤에 적는다.
배열 B의 subarray를 잡아 이들의 mex 값을 배열 $C$의 맨 뒤에 적는다.
이때 플레이어가 얻게 될 점수는 배열 $C$에 존재하는 모든 원소들의 mex값이다. 
'''


def BB():
    for i in range(len(A)):
        if i == (len(A) - 1):  # 마지막 경우까지 쫘라락 같은 경우에는
            return A[i] + 1
        elif (A[i] + 1) != A[i + 1]:
            return A[i] + 1  # B에 들어갈 수 있는 최댓값


n = int(input())
A = list(map(int, input().split()))

A = sorted(A)  # 오름차순
A = set(A)
A = list(A)
# print(A)

# A에 0이 없으면, 그리고 전부 0이면!!!!
# B에는 0밖에 못들어가고 C는 무조건 1만!!!들어갈 수 있다.
# C의 mex값은 0이다....
if A[0] != 0:
    print(0)
elif sum(set(A)) == 0:
    print(1)
else:
    print(BB() + 2)  # B

'''
#단순히 리스트의 mex를 구하는 것은, 아래처럼 set를 이용한 알고리즘이 효율적이다.
#하지만 이 문제에서는 여러 가지 조합이 나올 수 있고, 그 조합들을 이용한 mex값들의 리스트 중에서 또 mex값을 구하는 등
#mex값을 총 3번 구해야 하기 때문에, 
#모든 조합을 다 구하는 것보다는 규칙을 찾는 것이 효과적이었다.
n=int(input())
A = list(map(int, input().split()))

A=set(A) #세트로 바꾼다

h=0
for i in range(len(A)+1):
    if i not in A:
        h=i
        break
'''