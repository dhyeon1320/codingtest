def solution(A,B):
    a = sorted(A)
    b = sorted(B, reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += a[i]*b[i]
    return answer

print(solution([1,2],[3,4]))