# 220609
# 타일 채우기
# 3xN 크기의 벽을 2x1, 1x2 크기의 타일로 채우는 경우의 수

# 입력 : N (1 <= N <= 30)

# 출력 : 경우의 수

# dp[n] = dp[n-2] * 3 + dp[n-4] * 2 + dp[n-6] * 2 + ... + dp[2] * 2 + 2
# n이 홀수면 0
# n + 2가 될 때 마다 타일 모양이 2개 증가
# n = 2) 3
# n = 4) 3 * 3 + 2 = 11
# n = 6) dp[4] * 3 + dp[2] * 2 + 2 = 41
# dp[n-2] * 3 : dp[n-2] 타일에 dp[2] 타일 붙이기
# dp[n-k] * 2 : dp[n-k] 타일에 dp[k]의 새로운 타일(2종류) 붙이기 ~ 순서 반대로 붙이기

n = int(input())

dp = [0 for _ in range(30 + 1)]
dp[0] = 1

for i in range(2, n + 1, 2):
    dp[i] = dp[i-2] * 3
    for j in range(0, i - 2, 2):
        dp[i] += dp[j] * 2

print(dp[n])