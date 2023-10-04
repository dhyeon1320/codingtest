def solution(land):
    answer = 0
    dp = land
    for i in range(1, len(land)):
        for j in range(4):
            dp[i][j] = max(dp[i-1][:j] + dp[i-1][j+1:]) + dp[i][j]
    answer = max(dp[len(land)-1])

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer