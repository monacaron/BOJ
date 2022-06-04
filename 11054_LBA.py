# 220604
# 가장 긴 바이토닉 부분 수열
# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... Sn-1 > Sn을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
# 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램

# 입력1) 수열 A의 크기 N (1 <= N <= 1,000)
# 입력2) 수열 A를 이루고 있는 Ai ( 1 <= Ai <= 1,000)

# 출력 : 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이

# 정방향 LIS + 역방향 LIS

n = int(input())
a = list(map(int, input().split()))

ra = a[::-1] # 역방향 a

dp1 = [1 for _ in range(n)] # 정방향
dp2 = [1 for _ in range(n)] # 역방향

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if ra[i] > ra[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2.reverse()
result = 0
for i in range(n):
    # 최댓값 구하기
    if result < dp1[i] + dp2[i]:
        result = dp1[i] + dp2[i]

print(result - 1) # Sk 부분이 겹치니까 -1