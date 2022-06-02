# 220602
# 스타트와 링크
# 총 짝수 N명 ~ N/2명으로 이루어진 스타트 팀과 링크 팀으로 나누기
# 사람에게 1부터 N까지의 번호 배정
# Sij : i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치
# 팀의 능력치 = 팀에 속한 모든 쌍의 능력치 Sij의 합
# Sij != Sji 일 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij + Sji 이다.
# 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최솟값을 구하는 프로그램

# 입력1) N (4 <= N <= 20, N은 짝수)
# 입력2) N개의 줄에 S의 원소 입력
# i번 줄의 j번째 수는 Sij
# Sii는 항상 0이고, 나머지 Sij는 1 이상 100 이하의 정수

# 출력 : 스타트 팀과 링크 팀의 능력치의 차이 최솟값

# i번째 선수가 한 팀에 속하면 vistied[i] = True ~ 방문처리 해주면서 재귀함수 형태로 만들기
# 만약 한 팀에 속한 팀원의 수가 n//2로 다 채워졌으면 능력치 차이 구하기
# 스타트팀 : 방문o, 링크팀 : 방문x
# 능력치 차이의 절대값과 최소 능력치값을 비교하며 계속 갱신

import sys
sys.stdin = open("input.txt", "r")

def dfs(idx, depth):
    global min_diff # 최소 능력치 차이

    # n//2명을 모두 고른 경우
    if depth == n//2:
        p1, p2 = 0, 0 # 스타트팀 능력치, 링크팀 능력치
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # 방문o ~ 스타트팀
                if visited[i] and visited[j]:
                    p1 += s[i][j]
                # 방문x ~ 링크팀
                elif not visited[i] and not visited[j]:
                    p2 += s[i][j]
        min_diff = min(min_diff, abs(p1-p2))
        return

    for i in range(idx, n):
        if not visited[i]:
            # i번째 선수 선택o
            visited[i] = True
            dfs(i+1, depth+1)
            # i번째 선수 선택x
            visited[i] = False


n = int(input())

s = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    s.append(tmp)

visited = [False for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)

print(min_diff)