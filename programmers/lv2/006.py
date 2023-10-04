def solution(n):
    answer = 0
    for i in range(1,n+1):
        sum = 0
        int = i
        while sum<n:
            sum += int
            if sum==n:
                answer += 1
                break
            elif sum > n:
                break
            int += 1
    return answer

print(solution(15))