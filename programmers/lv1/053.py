def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5] * 2000
    onecorrect = 0
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    twocorrect = 0
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    threecorrect = 0
    for idx, i in enumerate(answers):
        if i == one[idx]:
            onecorrect += 1
        if i == two[idx]:
            twocorrect += 1
        if i == three[idx]:
            threecorrect += 1

    correct = [onecorrect, twocorrect, threecorrect]
    for idx, i in enumerate(correct):
        if max(correct) == correct[idx]:
            answer.append(idx + 1)
    return answer