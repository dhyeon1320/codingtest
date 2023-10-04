def solution(progresses, speeds):
    answer = []
    cnt = 0
    while True:
        if progresses == []:
            break
        progresses = [x+y for x,y in zip(progresses, speeds)]
        for idx, curr in enumerate(progresses):
            if curr >= 100:
                progresses[idx] = 100
            else:
                continue
        if progresses[0] == 100:
            for progress in progresses:
                if progress == 100:
                    cnt += 1
                else:
                    break
        if cnt > 0:
            answer.append(cnt)
            progresses = progresses[cnt:]
            speeds = speeds[cnt:]
            cnt = 0

    return answer

print(solution(	[1, 1, 50], [100, 2, 1]))