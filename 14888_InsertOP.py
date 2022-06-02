# 220602
# 연산자 끼워넣기
# N개의 수로 이루어진 수열 A1, A2, ..., An
# 수와 수 사이에 끼워넣을 수 있는 N - 1개의 연산자 ~ 덧셈, 뺄셈, 곱셈, 나눗셈
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
# 주어진 수의 순서를 바꿀 수 없음
# 나눗셈은 정수 나눗셈으로 몫만 취함

# 입력1) 수의 개수 N (2 <= N <= 11)
# 입력2) A1, A2, ..., An (1 <= Ai <= 100)
# 입력3) 합이 N-1인 4개의 정수 = 순서대로 덧셈, 뺄셈, 곱셈, 나눗셈의 개수

# 출력1) 식의 결과의 최댓값
# 출력2) 식의 결과의 최솟값

def dfs(x):
    global r1, r2
    global result
    
    # 연산자는 총 n - 1개
    # result와 비교하여 최댓값, 최솟값 갱신
    if x == n - 1:
        if r1 < result:
            r1 = result
        if r2 > result:
            r2 = result
        return
    
    for i in range(4):
        tmp = result 
        if op[i] > 0: # 연산자의 사용 개수 체크
            if i == 0: # +
                result += nums[x + 1]
            elif i == 1: # -
                result -= nums[x + 1]
            elif i == 2: # *
                result *= nums[x + 1]
            else: # /, 몫만 취함
                if result >= 0: # 양수 나누기
                    result //= nums[x + 1]
                else: # 음수 나누기
                    # 양수 나누기 후 음수로 변경
                    result = (-result//nums[x + 1]) * -1

            op[i] -= 1 # op[i] 사용한 경우
            dfs(x + 1) 
            result = tmp # 사용하지 않은 경우
            op[i] += 1

n = int(input())
nums = list(map(int, input().split())) # 수열 An
op = list(map(int, input().split())) # 연산자 개수

r1 = -int(1e9) # 최댓값
r2 = int(1e9) # 최솟값
result = nums[0]

dfs(0)

print(r1)
print(r2)