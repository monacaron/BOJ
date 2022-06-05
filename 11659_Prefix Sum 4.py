# 220605
# 구간 합 구하기 4
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램

# 입력1) 수의 개수 N, 합을 구해야 하는 횟수 M (1 <= N <= 100,000, 1 <= M <= 100,000)
# 입력2) N개의 수. 수는 1,000 이하의 자연수
# 입력3) M개의 줄에 걸쳐 합을 구해야 하는 구간 i와 j 입력 (1 <= i <= j <= N)

# 출력 : 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합 출력

import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] + nums
for x in range(1, n + 1):
    dp[x] += dp[x-1]

for test_case in range(1, m + 1):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])
