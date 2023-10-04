def solution(arr):
    answer = True
    arr.sort()
    for i in range(len(arr)):
        if arr[i] != i+1:
            return False

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer