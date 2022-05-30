# 220530
# 합분해
# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램
# 덧셈의 순서가 바뀐 경우는 다른 경우로 센다. 1 + 2 != 2 + 1
# 한 개의 수를 여러 번 쓸 수 도 있다.

# 입력 : N K (1 <= N <= 200, 1 <= K <= 200)

# 출력 : 답을 1,000,000,000으로 나눈 나머지

# 점화식 : dp[i][j] = dp[i - 1][j] + dp[i][j - 1] / i, j는 2 이상 ~ 테이블 그려서 확인
n, k = map(int, input().split())

dp = [[1 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(1, k + 1):
    dp[1][i] = i

a = 2
while a <= n:
    for i in range(2, k + 1):
        dp[a][i] = dp[a - 1][i] + dp[a][i - 1]
    a += 1

print(dp[n][k] % 1000000000)