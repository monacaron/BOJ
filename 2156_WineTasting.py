# 220603
# 포도주 시식
# 포도주 시식에는 다음과 같은 두 가지 규칙이 있다.
# 규칙1) 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 규칙2) 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
# 1부터 N까지의 번호가 붙어 있는 N개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램

# 입력1) 포도주 잔의 개수 N (1 <= N <= 10,000)
# 입력2) N개의 줄에 걸쳐 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다.
# 포도주의 양은 1,000 이하의 음이 아닌 정수

# 출력 : 최대로 마실 수 있는 포도주의 양

# 경우1) i번째 + dp[i-2]
# 경우1) i번째 + i-1번째 + dp[i-3]
# 경우3) i번째를 마시지 않는 경우 ~ dp[i-1]

n = int(input())

wine = [0] # 포도주의 양. 1부터 N까지의 번호 ~ 인덱스 0 사용 x
for _ in range(n):
    wine.append(int(input()))

dp = [0 for _ in range(10000 + 1)]

if n == 1:
    print(wine[1])
elif n == 2:
    print(wine[1] + wine[2])
elif n == 3:
    print(max(wine[2] + wine[1], wine[3] + wine[1], wine[3] + wine[2]))
else:
    dp[1], dp[2] = wine[1], wine[1] + wine[2]
    dp[3] = max(dp[2], wine[3] + dp[1], wine[3] + wine[2])

    for i in range(4, n + 1):
        dp[i] = max(wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3], dp[i-1])

    print(max(dp))