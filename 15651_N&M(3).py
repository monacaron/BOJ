# 220531
# N과 M(3)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 조건1) 1부터 N까지 자연수 중에서 M개를 고른 수열
# 조건2) 같은 수를 여러 번 골라도 된다.ㅏ

# 입력 : N M (1 <= M <= N <= 8)

# 출력 : 한 줄에 하나씩 문제의 조건을 만족하는 수열 출력
# 수열은 사전 순으로 증가하는 순서로 출력

def dfs():
    # m개를 뽑은 경우 출력 및 종료
    if len(k) == m:
        print(*k)
        return

    for i in arr:
        # 중복선택 상관x
        k.append(i) # arr[i]를 뽑은 경우
        dfs()
        k.pop() # arr[i]를 뽑지 않은 경우

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

k = []
dfs()