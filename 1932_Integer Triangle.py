# 220604
# 정수 삼각형
# 맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
# 삼각형의 크기는 1 이상 500 이하. 삼각형을 이루고 있는 각 수는 모두 정수. 범위는 0 이상 9999 이하

# 입력1) 삼각형의 크기 N (1 <= N <= 500)
# 입력2) N줄에 걸쳐 정수 삼각형 입력

# 출력 : 합이 최대가 되는 경로에 있는 수의 합

# 각 칸에 올 수 있는 최대값을 순차적으로 구하기

import sys
sys.stdin = open("input.txt")

n = int(input())

tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

dp = tri[::] # dp테이블 생성
for i in range(1, n):
    for j in range(len(dp[i])):
        if j > 0 and j < len(dp[i-1]) : # 삼각형 내부
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j]) # 위 층 왼쪽 수와 오른쪽 수를 비교하여 최대값 구하기
        elif j == 0: # 맨 왼쪽
            dp[i][j] += dp[i-1][j]
        else: # 맨 오른쪽
            dp[i][j] += dp[i-1][j-1]

print(max(dp[n-1])) # 마지막 줄의 최댓값 출력