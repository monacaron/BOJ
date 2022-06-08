# 220608
# 구간 합 구하기 5
# NxN개의 수가 NxN 크기의 표에 채워져 있다.
# (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램
# (x, y)는 x행 y열을 의미한다.
# 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램

# 입력1) 표의 크기 N 합을 구해야하는 횟수 M (1 <= N <= 1024, 1 <= M <= 100,000)
# 입력2) N개의 줄에 걸쳐 표 정보 입력
# 입력3) M개의 줄에 네 개의 정수 x1, y1, x2, y2 입력
# 표에 채워져 있는 수는 1,000 이하의 자연수
# x1 <= x2, y1 <= y2

# 출력 : 총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지의 합 출력

import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
table = [[0 for _ in range(n + 1)]] # 1행, 1열 시작

for _ in range(n):
    tmp = list(map(int, input().split()))
    tmp = [0] + tmp
    table.append(tmp)

for i in range(1, n + 1):
    for j in range(n + 1):
        table[i][j] += table[i-1][j]

for test_case in range(m):
    x1, y1, x2, y2 = map(int,input().split())

    result = sum(table[x2][y1:y2+1])
    result -= sum(table[x1-1][y1:y2+1])

    print(result)