# 220530
# 이항 계수 2
# 자연수 N과 정수 K가 주어졌을 때 이항 계수(N K)를 10,007로 나눈 나머지를 구하는 프로그램
# 이항 계수(N K) = nCk
# ex) (x + y)^2 = x^2 + 2xy + y^2 ~ 이항계수 = 각 항의 계수[1, 2, 1]

# 입력 : N K (1 <= N <= 1,000, 0 <= K <= N)

# 출력 : 이항 계수(N K)를 10,007로 나눈 나머지
import sys
sys.setrecursionlimit(10**6)

def facto(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * facto(x - 1)
n, k = map(int, input().split())

result = facto(n) // (facto(k) * facto((n - k)))

print(result % 10007)