def solution(s):
    answer = ""
    words = s.split(' ')
    for idx, word in enumerate(words):
        answer += word.capitalize()
        if idx != len(words)-1:
            answer += " "

    return answer

print(solution("3people unFollowed me"))