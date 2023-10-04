def solution(array, commands):
    answer = []
    for command in commands:
        start, finish, idx = command[0] - 1, command[1], command[2] - 1
        slicing = sorted(array[start:finish])
        answer.append(slicing[idx])

    return answer