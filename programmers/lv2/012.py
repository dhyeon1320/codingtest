from collections import deque

def solution(people, limit):
    answer = 0
    dq = deque(sorted(people))
    while len(dq) > 1 :
        light = dq[0]
        heavy = dq[-1]
        if limit < light+heavy:
            answer += 1
            dq.pop()
        else:
            answer += 1
            dq.pop()
            dq.popleft()
    if len(dq) == 1:
        answer += 1


    return answer

print(solution([70, 80 ,50, 60], 100))