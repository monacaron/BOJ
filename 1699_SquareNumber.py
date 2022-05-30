# 220530
# 제곱수의 합
# 어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다.
# 주어진 자연수 N을 제곱수들의 합으로 표현할 때, 그 항의 최소 개수를 구하는 프로그램
# 제곱수의 합 표현은 여러 가지가 될 수 있다.

# 입력 : 자연수 N (1 <= N <= 100,000)

# 출력 : 제곱수 항의 최소 개수

# 1) dp[제곱수] = 1
# dp[i] = min(dp[i], dp[i - j*j] + 1))
import math
n = int(input())

dp = [i for i in range(n + 1)]

k = 1
while k ** 2 <= n:
    dp[k ** 2] = 1
    k += 1

for i in range(2, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
print(dp[n])