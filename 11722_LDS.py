# 220609
# 가장 긴 감소하는 부분 수열
# 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램

# 입력1) 수열 A의 크기 N (1 <= N <= 1,000)
# 입력2) 수열 A를 이루고 있는 Ai (1 <= Ai <= 1,000)

# 출력 : 수열 A의 가장 긴 감소하는 부분 수열의 길이

# 역방향 LIS

n = int(input())
arr = list(map(int, input().split()))

arr.reverse()

dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))