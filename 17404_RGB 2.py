# 220610
# RGB거리 2
# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
# 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 다음 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구하는 프로그램
# 규칙1) 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
# 규칙2) N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# 규칙3) i(2 <= i <= N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

# 입력1) 집의 수 N (2 <= N <= 1,000)
# 입력2) N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
# 집을 칠하는 비용은 1,000 이하의 자연수

# 출력 : 모든 집을 칠하는 비용의 최솟값

# 1번 집의 색을 미리 정하고 dp 구하기

import sys
sys.stdin = open("input.txt", "r")
INF = int(1e9)

n = int(input())

house = []
for _ in range(n):
    house.append(list(map(int, input().split())))

house = [[0, 0, 0]] + house

result = INF

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n+1)] # 0번 집 사용 x
    dp[1][i] = house[1][i] # 1번 집을 r, g, b 중 하나로 색칠

    # 해당 경우에 집을 칠하는 비용
    for j in range(2, n + 1):
        dp[j][0] = house[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = house[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = house[j][2] + min(dp[j-1][0], dp[j-1][1])

    # 1번 집과 N번 집을 다르게 칠하는 경우에서 최솟값 갱신
    for j in range(3):
        if j != i:
            result = min(result, dp[n][j])

print(result)