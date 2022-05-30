# 220530
# 이항 계수 1
# 자연수 N과 정수 K가 주어졌을 때, 이항 계수(N K)를 구하는 프로그램

# 입력 : N K (1 <= N <= 10, 0 <= K <= N)

# 출력 : 이항 계수(N K)

def facto(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * facto(x - 1)
n, k = map(int, input().split())

result = facto(n) // (facto(k) * facto((n - k)))

print(result)