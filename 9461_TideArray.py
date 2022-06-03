# 220603
# 파도반 수열
# 나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형 추가
# 파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이
# N이 주어졌을 때, P(N)을 구하는 프로그램

# 입력1) 테스트 케이스 개수 T
# 입력2) N (1 <= N <= 100)

# 출력 : P(N)

# 점화식 : dp[i] = dp[i-2] + dp[i-3]
# dp[1], dp[2], dp[3] = 1, 1, 1

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    dp = [0 for _ in range(100 + 1)]
    dp[1], dp[2], dp[3] = 1, 1, 1

    for k in range(4, n + 1):
        dp[k] = dp[k-2] + dp[k-3]

    print(dp[n])