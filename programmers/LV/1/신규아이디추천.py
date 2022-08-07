def solution(new_id):
    answer = new_id.lower()  # 1단계

    A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']

    answer2 = ''
    for i in range(len(answer)):  # 2단계
        if answer[i] in A:
            answer2 += answer[i]

    # 4단계
    if answer2[0] == '.':
        answer2 = answer2[1:]
    if answer2 == '':
        answer2 = 'a'
    if answer2[-1] == '.':
        answer2 = answer2[:-1]
    if answer2 == '':
        answer2 = 'a'
    answer3 = answer2[0]

    for i in range(1, len(answer2)):  # 3단계
        if answer2[i] == '.':
            if answer2[i - 1] != '.':
                answer3 += answer2[i]
        else:
            answer3 += answer2[i]
    # print(answer3)
    # 4단계
    if answer3[0] == '.':
        answer3 = answer3[1:]
    if answer3 == '':
        answer3 = 'a'
    if answer3[-1] == '.':
        answer3 = answer3[:-1]

    # 5단계
    if answer3 == '':
        answer3 = 'a'

    # 6단계
    if len(answer3) >= 16:
        answer3 = answer3[:15]
    if answer3[0] == '.':
        answer3 = answer3[1:]
    if answer3 == '':
        answer3 = 'a'
    if answer3[-1] == '.':
        answer3 = answer3[:-1]
    if answer3 == '':
        answer3 = 'a'

    # 7단계
    while len(answer3) <= 2:
        answer3 += answer3[-1]

    return answer3

# print(solution(".A..B..-CD*7.."))
# print(solution("......................."))