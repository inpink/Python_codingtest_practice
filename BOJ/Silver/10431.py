import sys
input = sys.stdin.readline

p = int(input())
for a in range(p):
  students = list(map(int, input().split()))[1:]
  count=0

  end=19
  while True:
    if end==0:
      break
    for i in range(0,end+1):
      if (students[i] > students[end]):
        # print(end, end-i, i, students)
        count+=(end-i)
        pop = students.pop(end)
        students.insert(i,pop)
        continue
    end-=1

  print(a+1, count)



'''
 키 순서대로 번호를 부여'
  키가 가장 작은 아이가 1번
  같은 키를 가진 학생은 한 명도 없어

  우선 아무나 한 명을 뽑아 줄의 맨 앞에 세운다.
  자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
  자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다. 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.

  이 과정을 반복하면 결국 오름차순으로 줄을 설 수가 있다.

  위의 방법을 마지막 학생까지 시행하여 줄서기가 끝났을 때 학생들이 총 몇 번 뒤로 물러서게 될까?

  무조건20명
'''