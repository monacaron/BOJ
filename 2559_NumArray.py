# 220605
# 수열
# 매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램

# 입력1) 전체 날짜 수 N, 연속적인 날짜의 수 K (2 <= N <= 100,000)
# 입력2) 매일 측정한 온도를 나타내는 N개의 정수. 모두 -100 이상 100 이하

# 출력 : 연속적인 K일의 온도의 합이 최대가 되는 값

import sys
sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
temp = list(map(int, input().split()))

result = sum(temp[:k])

start = 0
end = k
tmp = result
for _ in range(n - k):
    tmp = tmp - temp[start] + temp[end]
    if result < tmp:
        result = tmp
    start += 1
    end += 1

print(result)