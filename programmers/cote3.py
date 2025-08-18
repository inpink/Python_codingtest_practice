from collections import Counter


def max_jelly_pockets(pouches):
  # 각 주머니에 있는 젤리 개수를 카운트하여 리스트로 저장합니다.
  counters = []
  for pouch in pouches:
    counter = Counter(pouch)
    counters.append(counter)

  # 가능한 최대 주머니의 개수를 기록
  answer = 0
  print(counters)

  # 각 젤리 맛 'a', 'b', 'c', 'd', 'e' 를 기준으로 최대 선택 가능한 주머니 수를 계산
  for jelly in "abcde":
    # 특정 젤리 맛을 기준으로 초기화
    selected = []
    target = 0
    others = 0

    # 특정 젤리 맛 기준으로 이득을 계산하고 정렬
    # gain = 해당 젤리 맛 개수 - 다른 젤리 맛 개수
    gain = []
    for pouch in counters:
      target_count = pouch[jelly]
      print(pouch.values())
      other_count = sum(pouch.values()) - target_count
      gain.append((target_count - other_count, target_count, other_count))

    # 이득(gain)을 기준으로 내림차순 정렬 (최대 이득부터)
    gain.sort(reverse=True, key=lambda x: (x[0], x[1]))
    print("gains",gain)

    # 그리디하게 주머니를 추가하며 조건을 만족하는지 체크
    for gain_count, target_count, other_count in gain:
      if target + target_count > others + other_count:
        target += target_count
        others += other_count
        selected.append((gain_count, target_count, other_count))
      else:
        break

    # 현재 젤리 맛 기준으로 선택된 주머니의 개수를 업데이트
    answer = max(answer, len(selected))
  print()
  return answer


# 예시 테스트
print(max_jelly_pockets(["cab", "adaaa", "e"]))  # Output: 3
print(max_jelly_pockets(["aabb", "baba"]))  # Output: 0
print(max_jelly_pockets(["d", "a", "e", "d", "abdcc"]))  # Output: 3
print(max_jelly_pockets(["d", "d", "a"]))  # Output: 3
print(max_jelly_pockets(["a"])) # Output: 1
print(max_jelly_pockets(["a","a","a","a","a"]))  # Output: 5
print(max_jelly_pockets(["ab","cd","ee"])) # Output: 1
print(max_jelly_pockets(["ab","ab","cc"])) # Output: 1

'''
젤리를 쉽게 가져갈 수 있도록 주머니에 미리 나누어 담아둡니다
5가지의 젤리가 있다 a,b,c,d,e 

+""최대한 많은 젤리 주머니""를 가져가고 싶었다
+모든 주머니의 젤리 꺼내 모았을 때, ""어떤 한 가지 맛의 젤리를 다른 젤리의 개수를 모두 합 보다 많아야 함""

모든 주머니의 모든 젤리 개수는 20만개까지
모든 젤리 주머니에는 최소 1개 이상의 젤리가 들어있음

* 얼마나 많은 젤리 주머니를 가져갈까?


예시1)
["cab","adaaa", "e"]
3주머니 모두 선택하면 
a젤리 5개 >  b+c+d+e 젤리 4개  => OK
return 3 OK

예시 2)
["aabb","baba"]
어떻게 선택해도
a젤리 개수 = b젤리 => 불가능
return 0

예시 3)
d, a, e, d, abdcc
d, d, a 또는 d, d, e 또는 d,d, abdcc
3주머니 선택하면 가능
return 0


당연히 완탐안됨


'''
