# 220605
# 인간-컴퓨터 상호작용
# 특정 문자열 S, 특정 알파벳 a와 문자열 구간 [l, r]이 주어지면 S의 l번째 문자부터 r번째 문자 사이에 a가 몇 번 나타나는지 구하는 프로그램
# 문자열의 문자는 0번째부터 세며, l번째와 r번째 문자를 포함해서 생각한다.

# 입력1) 문자열 S. 문자열의 길이는 200,000자 이하이며 알파벳 소문자로만 구성되었다.
# 입력2) 질문의 수 Q (1 <= Q <= 200,000)
# 입력3) Q줄에 걸쳐 질문 알파벳 a, 구간 l, r 입력
# 각 질문은 알파벳 소문자 ai와 0 <= li <= ri < |S|를 만족

# 출력 : i번째 줄에 S의 li번째 문자부터 ri번째 문자 사이에 ai가 나타나는 횟수 출력

# PyPy로 제출해야 100점

import sys
sys.stdin = open("input.txt", "r")

s = input()
q = int(input())

alpha = []
for i in range(26):
    alpha.append(chr(97 + i))

dp = [[0 for _ in range(26)] for _ in range(len(s))]

dp[0][ord(s[0])-97] = 1

for i in range(1, len(s)):
    dp[i][ord(s[i]) - 97] = 1
    for j in range(26):
        dp[i][j] += dp[i-1][j]

for test_case in range(q):
    a, l, r = map(str, input().split())
    l = int(l)
    r = int(r)

    if l == 0 :
        print(dp[r][ord(a) - 97])
    else:
        print(dp[r][ord(a) - 97] - dp[l-1][ord(a) - 97])