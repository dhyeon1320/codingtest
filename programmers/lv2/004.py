def solution(s):
    check = []
    for i in s:
        if i =="(":
            check.append(i)
        else:
            if check == []:
                answer = False
            else:
                check.pop()
    return check == []