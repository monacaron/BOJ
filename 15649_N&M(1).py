# 220531
# N과 M(1)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 조건1) 1부터 N까지의 자연수 중에서 중복 없이 M개를 고른 수열

# 입력: N M (1 <= M <= M <= 8)

# 출력 : 한 줄에 하나씩 문제의 조건을 만족하는 수열 출력
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 백트래킹
def dfs():
    # m개를 모두 선택했다면 결과 출력 및 종료
    if len(k) == m:
        print(*k)
        return

    # 가지치기
    for i in arr:
        if i in k: # 이미 arr[i]를 선택했다면 넘어가기
            continue
        k.append(i) # arr[i]를 선택한 경우에 대해서 백트래킹
        dfs()
        k.pop() # 다음 수행을 위해 리스트 비우기

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)] # 1 ~ N

k = []
dfs()