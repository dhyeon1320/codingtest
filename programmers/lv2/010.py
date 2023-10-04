def solution(brown, yellow):
    answer = []
    tot = brown+yellow
    limit = tot//2 + 1
    for i in range(3, limit):
        if tot%i == 0:
            w = int(tot/i)
            h = int(i)
            if (w-2)*(h-2) == yellow:
                answer.append(w)
                answer.append(h)
                break
    return answer

print(solution(24,24))