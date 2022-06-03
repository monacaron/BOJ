# 220603
# 알고리즘 수업 - 피보나치 수 1
# 제공된 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1, 코드2 실행 횟수를 출력하는 프로그램

# 입력 : n (5 <= n <= 40)

# 출력 : 코드1, 코드2 실행 횟수를 한 줄에 출력

# code1
def fib(n):
    global cnt1

    if n == 1 or n == 2:
        return 1
    else:
        cnt1 += 1
        return fib(n-1) + fib(n-2)

# code2
def fibonacci(n):
    global cnt2

    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        f[i] = f[i-1] + f[i-2]
        cnt2 += 1
    return f[n]

n = int(input())

f = [0 for _ in range(n + 1)]

cnt1 = 0 # code1 실행횟수
cnt2 = 0 # code2 실행횟수

fib(n)
fibonacci(n)

print(cnt1 + 1, cnt2)