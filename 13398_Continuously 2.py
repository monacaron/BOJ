# 220609
# 연속합2
# N개의 정수로 이루어진 임의의 수열
# 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하는 프로그램
# 단, 수는 한 개 이상 선택해야 하며, 수열에서 수를 하나 제거할 수 있다.(제거하지 않아도 된다.)
# ex) 10, -4, 3, 1, 5, 6, -35, 12, 21, -1
# 수를 제거하지 않은 경우 : 12 + 21 = 33
# 수를 하나 제거한 경우 : -35 제거 ~ 10 + ... + -1 = 54

# 입력1) 정수 N (1 <= N <= 100,000)
# 입력2) N개의 정수로 이루어진 수열. -1,000 이상 1,000 이하의 정수

# 출력 : 가장 큰 합

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))

# dp[0] : 특정 원소를 제거하지 않은 경우
# dp[1] : 특정 원소를 제거한 경우
# 한 개 이상 선택 ~ 본인만 고르는 경우
dp = [[arr[i] for i in range(n)] for _ in range(2)]

for i in range(1, n):
    # 원소를 제거하지 않은 경우
    dp[0][i] = max(dp[0][i], arr[i] + dp[0][i-1])

    # 특정 원소를 제거하는 경우
    # dp[0][i-1] : i번째 원소를 제거하는 경우
    # dp[1][i-1] + arr[i] : i번째 이전에 원소를 제거한 경우 중 최대값 + i번째 원소
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])

result = max(max(dp[0]), max(dp[1]))

print(result)