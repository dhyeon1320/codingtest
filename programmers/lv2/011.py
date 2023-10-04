def solution(n, words):
    answer1 = [0,0]
    answer2 = [0,0]
    order = [(i%n)+1 for i in range(len(words))]
    for idx in range(len(words)-1):
        if words[idx][-1] != words[idx+1][0]:
            answer1[0] = order[idx+1]
            answer1[1] = int((idx+1)//n) + 1
            break
    for idx in range(len(words)):
        if words[idx] in words[:idx]:
            answer2[0] = order[idx]
            answer2[1] = int((idx)//n) + 1
            break

    if answer1 == [0,0] and answer2 == [0,0]:
        answer = answer1
    elif answer1 != [0,0] and answer2 !=[0,0]:
        if answer1[1] < answer2[1]:
            answer = answer1
        elif answer1[1] > answer2[1]:
            answer = answer2
        elif answer1[1] == answer2[1]:
            if answer1[0] <= answer2[0]:
                answer = answer1
            else:
                answer = answer2
    else:
        if answer1[0] > 0:
            answer = answer1
        else:
            answer = answer2

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
print(solution(4, ["hello", "one", "even", "even", "now", "draw"]))
print(solution(2, ["hello", "one", "even", "never", "row", "world", "draw"]))
print(solution(2, ["qws", "sqwes", "sqwe"]))
print(solution(2, ["qws", "sqsqwes", "sqwes"]))
print(solution(2, ["qws", "sqsqwess", "sqwes"]))
print(solution(3, ["tank", "tick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["land", "dream", "mom", "mom", "ror"]))
print(solution(2, ["land", "dream", "mom", "mom"]))
print(solution(2, ['ac','ca','ac','ac']))