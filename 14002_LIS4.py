# 220530
# 가장 긴 증가하는 부분 수열 4
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램

# 입력1) 수열 A의 크기 N (1 <= N <= 1,000)
# 입력2) 수열 A를 이루고 있는 Ai (1 <= Ai <= 1,000)

# 출력1) 수열 A의 가장 긴 증가하는 부분 수열의 길이
# 출력2) 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 뒤에서 부터 확인
k = max(dp)
result = []
for i in range(n-1, -1, -1):
    if dp[i] == k:
        result.append(arr[i])
        k -= 1

result.reverse()
print(len(result))
print(*result)