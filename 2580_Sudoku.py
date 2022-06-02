# 220602
# 스도쿠
# 게임 시작 전 스도쿠 판에 쓰여있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램

# 입력 : 아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자를 공백으로 구분하여 입력
# 빈 칸의 경우 0
# 스도쿠 판을 규칙대로 채울 수 있는 경우만 입력됨

# 출력 : 모든 빈 칸이 채워진 스도쿠 판의 최종 모습
# 채우는 방법이 여럿인 경우 그 중 하나만을 출력

# 가로, 세로, 3 x 3 사각형

import sys
sys.stdin = open("input.txt", "r")

# 행, 열, 3 x 3 사각형 체크
def isPromising(x, y):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 빈 칸에 들어갈 수 있는 수
    for k in range(9):
        # 열
        if arr[k][y] in nums:
            nums.remove(arr[k][y])
        # 행
        if arr[x][k] in nums:
            nums.remove(arr[x][k])
    # 3 x 3 박스
    x //= 3
    y //= 3
    for i in range(x*3, (x+1)*3):
        for j in range(y*3, (y+1)*3):
            if arr[i][j] in nums:
                nums.remove(arr[i][j])

    return nums

def dfs(x):
    global flag

    # 정답이 한 번 출력되었다면 종료
    #if flag:
    #    return
    # 마지막 칸까지 모두 채웠다면 결과 출력
    if x == len(zero):
        for row in arr:
            print(*row)
        flag = True
        exit() # flag 대신 exit() 사용해야 시간 초과 x
        #return
    else:
        # 빈 칸의 좌표
        (i, j) = zero[x]
        # 빈 칸에 넣을 수 있는 수
        nums = isPromising(i, j)
        # 각 경우의 수를 확인
        for num in nums:
            arr[i][j] = num # 가능한 숫자 중 하나를 넣기
            dfs(x + 1) # 다음 빈 칸 채우기
            arr[i][j] = 0 # 다음 경우를 위해 초기화

arr = [] # 스도쿠 판
for _ in range(9):
    arr.append(list(map(int, input().split())))

# 빈 칸인 곳의 좌표 리스트
zero = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]
flag = False # 결과 출력 여부

dfs(0)