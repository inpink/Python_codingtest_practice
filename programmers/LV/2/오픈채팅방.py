def solution(record):
    answer = []
    lenn=len(record)
    Enters={}
    for i in range(lenn): #모든 요소에 대해 반복
        if record[i][0]=="E": #Enter일 경우
            help=record[i].split() #['Enter', 'uid1234', 'Muzi']
            Enters[help[1]]=help[2]
            answer.append([help[1],"E"]) #uid와 E를 입력
        elif record[i][0]=="L": #Leave일 경우
            help=record[i].split()
            answer.append([help[1],"L"])
        else : #Change일 경우
            help=record[i].split()
            Enters[help[1]]=help[2]

    #print(Enters, answer)
    #E={'uid1234': 'Prodo', 'uid4567': 'Ryan'}
    #ans=[['uid1234', 'E'], ['uid4567', 'E'], ['uid1234', 'L'], ['uid1234', 'E']]
    lenn=len(answer)
    a=[]
    for i in range(lenn): #다시 반복하여 result 완성
        help=Enters[answer[i][0]]
        #print(answer[i][1], lenn)
        if answer[i][1]=="E": #Enter일 경우
            a.append(help+"님이 들어왔습니다.")
        else: #Leave일 경우
            a.append(help+"님이 나갔습니다.")
    #print(Enters, answer,a)
    return a
#문제 URL https://school.programmers.co.kr/learn/courses/30/lessons/42888

record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

solution(record)
