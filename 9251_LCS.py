# 220604
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)
# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 프로그램
# ex) ACAYKP, CAPCAK => ACAK

# 입력1) 문자열 A
# 입력2) 문자열 B
# 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

# 출력 : 주어진 두 문자열의 LCS의 길이

a = input()
b = input()

dp = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]

for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if b[i - 1] == a[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])