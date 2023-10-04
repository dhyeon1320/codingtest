def solution(bridge_length, weight, truck_weights):
    answer = 0
    onbridge = []
    finish = []
    while len(truck_weights) > 0:
        answer += 1
        truck = truck_weights.pop(0)
        onbridge.append(truck)
        if sum(onbridge) + truck_weights[0] > weight:
            answer += 1
            fin = onbridge.pop(0)
            finish.append(fin)
        else:
            pass

    return answer

print(solution(2, 10, [7,4,5,6]))