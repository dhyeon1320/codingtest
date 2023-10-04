def solution(board):
    answer = 0
    m = len(board)
    n = len(board[0])
    for i in range(1, m):
        for j in range(1, n):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1

    for i in range(m):
        num = max(board[i])
        answer = max(answer, num)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer ** 2