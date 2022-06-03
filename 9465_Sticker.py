# 220603
# 스티커
# 스티커 2 * n개 ~ 2행 n열로 배치
# 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 사용 불가 ~ 즉, 뗀 스티커와 인접한 스티커는 사용 불가
# 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내는 프로그램

# 입력1) 테스트 케이스 개수 T
# 입력2) N (1 <= N <= 100,000)
# 입력3) 두 줄에 걸쳐 N개의 정수 입력 ~ 각 정수는 그 위치에 해당하는 스티커의 점수
# 점수는 0 이상 100 이하의 정수

# 출력 : 각 테스트 케이스 마다, 2 * n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값 출력

# dp[0][i] = s[0][i] + max(dp[1][i-1], dp[0][i-2], dp[1][i-2])
# dp[1][i] = s[1][i] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])
# 총 3가지 경우 비교
#import sys
#sys.stdin = open("input.txt", "r")
t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    s = [] # 스티커 점수
    for _ in range(2):
        s.append(list(map(int, input().split())))

    dp = s[::]

    if n == 1:
        r1 = max(dp[0])
        r2 = max(dp[1])

        if r1 >= r2:
            print(r1)
        else:
            print(r2)

    elif n == 2:
        dp[0][1] = s[0][1] + s[1][0]
        dp[1][1] = s[1][1] + s[0][0]

        r1 = max(dp[0])
        r2 = max(dp[1])

        if r1 >= r2:
            print(r1)
        else:
            print(r2)

    else:
        dp[0][1] = s[0][1] + s[1][0]
        dp[1][1] = s[1][1] + s[0][0]

        for i in range(2, n):
            dp[0][i] = s[0][i] + max(dp[1][i-1], dp[0][i-2], dp[1][i-2])
            dp[1][i] = s[1][i] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])

        r1 = max(dp[0])
        r2 = max(dp[1])

        if r1 >= r2:
            print(r1)
        else:
            print(r2)