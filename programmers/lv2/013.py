def solution(n):
    ans = 0
    binary = bin(n)[2:]
    ans = binary.count('1')

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return ans

print(solution(5000))