# 220608
# 나머지 합
# 수 N개 A1, A2, ..., AN이 주어진다.
# 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램
# 즉, Ai + ... + Aj (i <= j)의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구하는 프로그램

# 입력1) N M (1 <= N <= 1e6, 2 <= M <= 1e3)
# 입력2) N개의 수 A1, A2, ..., AN (0 <= Ai <= 1e9)

# 출력 : 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cntlist = [0 for _ in range(m)]
# cntlist[0] = 1

result = 0

for i in range(n):
    result += arr[i]

    cntlist[result%m] += 1 # index를 나머지로 가지는 수의 개수

cnt = 0
for i in cntlist:
    # nCr = n! / r!(n-r)!
    # nC2 = n(n-1) / 2
    cnt += i * (i-1) // 2

print(cnt + cntlist[0]) # cntlist[0] : 해당 수 자체가 m의 배수인 경우