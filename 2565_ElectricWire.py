# 220604
# 전깃줄
# 전깃줄의 개수와 전깃줄들이 두 번봇대에 연결되는 위치의 번호가 주어질 때, 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램

# 입력1) 두 전봇대 사이의 전깃줄의 개수 N. N은 100 이하의 자연수
# 입력2) N줄에 걸쳐 A전봇대와 연결되는 위치의 번호와 B전봇대와 연결되는 위치의 번호를 차례대로 입력
# 위치의 번호는 500 이하의 자연수. 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.

# 출력 : 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수
import sys
sys.stdin = open("input.txt", "r")

n = int(input()) # 전깃줄 개수
wire = [0 for _ in range(500 + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    wire[a] = b

dp = [0 for _ in range(500 + 1)]
for i in range(500 + 1):
    if wire[i]:
        dp[i] = 1

for i in range(1, 500 + 1):
    for j in range(i):
        if wire[i] > wire[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(wire)
print(dp)
print(n - max(dp))