def solution(participant, completion):
    dic = {}
    for name in participant:
        if name not in dic:
            dic[name] = 1
        else:
            dic[name] += 1
    for complete in completion:
        dic[complete] -= 1
    for key, value in dic.items():
        if value == 1:
            answer = key
    return answer