# 220604
# 평범한 배낭
# 여행에 필요하다고 생각하는 N개의 물건
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 V만큼 즐길 수 있다.
# 최대 K만큼의 무게만을 넣을 수 있는 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 구하는 프로그램

# 입력1) 물품의 수 N, 제한 최대 무게 K (1 <= N <= 100, 1 <= K <= 100,000)
# 입력2) N개의 줄에 걸쳐 각 물건의 무게 W와 해당 물건의 가치 V 입력 (1 <= W <= 100,000, 0 <= V <= 1,000)
# 입력으로 주어지는 모든 수는 정수

# 출력 : 배낭에 넣을 수 있는 물건들의 가치합의 최댓값

# 다이나믹 프로그래밍 유형 - Knapsack
# 경우1) i번째 물건을 넣었을 때 무게 초과 ~ i번째 물건 x ~ 이전 가치
# 경우2) i번째 물건을 넣었을 때 무게 초과 x ~ max(이전 가치, 새로운 가치)
import sys
sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())

items = [] # (w, v)
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v)) # 물건의 가치와 무게를 튜플로 저장

# i 번째까지 탐색했을 때, 무게가 j인 가방의 최대 가치
dp = [[0 for _ in range(k + 1)] for _ in range(n)]
# 첫 번째 가방의 경우
for i in range(k + 1):
    if items[0][0] <= i: # 변수 i ~ 무게(i)가 items[0][0]보다 클 때만
        dp[0][i] = items[0][1] # dp테이블 갱신

for i in range(1, n): # 두 번째 가방 ~ 마지막 가방
    for j in range(1, k + 1): # 무게 1 ~ k
        if items[i][0] > j: # 무게 초과 ~ 새로운 물건 x
            dp[i][j] = dp[i-1][j] # 이전 가치
        else: # 이번 물건을 넣을 수 있는 경우
            # max(이번 물건 x, 이번 물건 o)
            # 이번 물건 x = 이전 가치
            # 이번 물건 o = 이번 물건을 넣기 위해 필요한 무게 w를 뺀 dp[i-1][j-w]에 이번 물건의 가치 v를 추가
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][0]]+items[i][1])

print(dp[-1][-1])