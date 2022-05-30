# dp 이용
def facto():
    i = 1
    while i < 30 + 1:
        dp[i] = i * dp[i - 1]
        i += 1

t = int(input())

dp = [0 for _ in range(30 + 1)]
dp[0], dp[1] = 1, 1
facto()

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    result = dp[m] // (dp[n] * dp[m - n])

    print(result)