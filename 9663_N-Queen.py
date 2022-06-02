# 220602
# N-Queen
# N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램

# 입력 : N (1 <= N <= 15)

# 출력 : 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수

# 해당 위치에 퀸을 놓을 수 있는지 확인
# 가로, 세로, 대각
def isPromising(x):
    for i in range(x):
        # chess[x] == chess[i] : 같은 열에 놓은 경우
        # abs(chess[x] - chess[i]) == x - i : 대각선에 놓은 경우
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == x - i:
            return False
    return True

def queens(x):
    global result

    # N개를 다 놓은 경우
    if x == n:
        result += 1
        return

    for i in range(n):
        chess[x] = i
        # x행 i열에 놓을 수 있는지 확인
        if isPromising(x):
            queens(x + 1)

n = int(input())
result = 0

chess = [0 for _ in range(n)] # chess[x] = y : x행 y열에 위치
queens(0)
print(result)