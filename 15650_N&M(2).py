# 220531
# N과 M(2)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 조건1) 1부터 N까지의 자연수 중에서 중복 없이 M개를 고른 수열
# 조건2) 고른 수열은 오름차순이어야 한다.

# 입력 : N M (1 <= M <= N <= 8)

# 출력 : 한 줄에 하나씩 문제의 조건을 만족하는 수열 출력
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

def dfs(idx):
    # m개를 모두 뽑은 경우 출력 및 종료
    if len(k) == m:
        print(*k)
        return
    # idx가 범위를 벗어나는 경우 종료
    if idx >= n:
        return
    # arr[idx]를 선택한 경우
    k.append(arr[idx])
    dfs(idx + 1)
    # arr[idx]를 선택하지 않은 경우
    k.remove((arr[idx]))
    dfs(idx + 1)

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

k = []
dfs(0)