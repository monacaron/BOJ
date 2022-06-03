# 220603
# 신나는 함수 살행
# a, b, c가 주어졌을 때 w(a, b, c)를 출력하는 프로그램

# 입력 : 세 정수 a, b, c
# 입력의 마지막은 -1 -1 -1

# 출력 : 각각의 a, b, c에 대해서 w(a, b, c) 출력

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

dp = [[[0 for _ in range(20 + 1)] for _ in range(20 + 1)] for _ in range(20 + 1)]
while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')