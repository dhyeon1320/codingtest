def solution(s):
    answer = [0,0]
    new_s = ""
    while True:
        if s == "1":
            break
        for i in s:
            if i == "0":
                answer[1] += 1
            else:
                new_s += i
        s = str(bin(len(new_s))[2:])
        new_s = ""
        print(type(s))
        answer[0] += 1
    return answer

print(solution("110010101001"))