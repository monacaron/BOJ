# 220627
# 동전 0
# 동전은 총 N종류
# 동전을 적절히 사용해서 그 가치의 합을 K로 만드려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램

# 입력1) N K (1 <= N <= 10, 1 <= K <= 100,000,000)
# 입력2) N개의 줄에 걸쳐 동전의 가치 Ai가 오름차순으로 주어진다.(1 <= Ai <= 1,000,000, A1 = 1, i >= 2인 경우에는 Ai는 Ai-1의 배수)

# 출력 : K원을 만드는데 필요한 동전 개수의 최솟값

n, k = map(int, input().split())
coin = []

for _ in range(n):
    coin.append(int(input()))

coin.reverse()
result = 0
for i in range(n):
    result += k // coin[i]
    k %= coin[i]
    if k == 0:
        break

print(result)