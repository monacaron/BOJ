# 220531
# 1, 2, 3 더하기 3
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램

# 입력1) 테스트 케이스 개수 T
# 입력2) 정수 n. n은 양수이며 1,000,000보다 작거나 같다.

# 출력 : n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지

# 점화식 : dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# 1, 2, 3 차이가 나는 경우의 수 + 1, 2, 3을 한다는 가정
# dp[1], dp[2], dp[3] = 1, 2, 4

mod = int(1e9) + 9
INF = int(1e6)

t = int(input())

dp = [0 for _ in range(INF + 1)]
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, INF + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % mod

print(dp)
for test_case in range(1, t + 1):
    n = int(input())
    print(dp[n] % mod)