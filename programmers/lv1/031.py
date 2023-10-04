def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for idx, num in enumerate(arr):
        if idx == 0:
            answer.append(num)
        elif num != arr[idx-1]:
            answer.append(num)
    return answer