# 220530
# 연속합
# n개의 정수로 이루어진 임의의 수열
# 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하는 프로그램

# 입력1) 정수 n (1 <= n <= 100,000)
# 입력2) n개의 정수로 이루어진 수열. 수는 -1,000 이상 1,000 이하의 정수

# 출력 : 최대 합

n = int(input())
nums = list(map(int, input().split()))

dp = nums[::]

for i in range(1, n):
    dp[i] = max(dp[i], dp[i] + dp[i - 1])

print(max(dp))