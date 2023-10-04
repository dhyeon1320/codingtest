import math
def solution(n,a,b):
    answer = 0
    m = int(math.log(n,2))
    left = min(a,b)
    right = max(a,b)
    while m >= 1:
        if n/2 in range(left, right+1) :
            answer = m
            break
        else:
            if right <= n/2 :
                m -= 1
                n = n/2
            elif left >= n/2 :
                m -= 1
                n = n*3/2

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer

print(solution(32,1,16))