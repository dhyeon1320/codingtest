def solution(s):
    answer = []
    for al in s:
        if answer == []:
            answer.append(al)
        elif len(answer)>0:
            if answer[-1] == al:
                answer.pop()
            else:
                answer.append(al)
    if answer == []:
        return 1
    else:
        return 0


    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

print(solution("cdcd"))