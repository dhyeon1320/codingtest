def solution(sticker):
    answer = 0
    if len(sticker) > 2:
        dp1 = [0 for _ in sticker]
        dp1[0] = sticker[0]
        dp1[1] = dp1[0]
        dp2 = [0 for _ in sticker]
        dp2[0] = 0
        dp2[1] = sticker[1]
        for i in range(2, len(sticker) - 1):
            dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])
        for i in range(2, len(sticker)):
            dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])

        answer = max(max(dp1), max(dp2))

    else:
        answer = max(sticker)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer