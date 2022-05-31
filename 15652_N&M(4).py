# 220531
# N과 M(4)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 조건1) 1부터 N까지의 자연수 중에서 M개를 고른 수열
# 조건2) 같은 수를 여러 번 골라도 된다.
# 조건3) 고른 수열은 비내림차순이어야 한다.
# 비내림차순 : 길이가 K인 수열 A가 A1 <= A2 <= ... <= Ak-1 <= Ak를 만족

# 입력 : N M (1 <= M <= N <= 8)

# 출력 : 한 줄에 하나씩 문제의 조건을 만족하는 수열 출력
# 수열은 사전 순으로 증가하는 순서로 출력

def dfs(idx):
    if len(k) == m:
        print(*k)
        return

    for i in range(idx, n): # 선택하는 원소의 범위를 arr[idx] ~ arr[n-1]로 좁히기
        k.append(arr[i]) # arr[i] 선택
        dfs(i) # arr[i]보다 작은 원소는 선택 x
        k.pop()

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

k = []
dfs(0)