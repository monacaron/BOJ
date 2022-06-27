# 220627
# 회의실 배정
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾는 프로그램
# 단, 회의는 한 번 시작하면 중간에 중단되지 않으며, 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다.

# 입력1) 회의의 수 N(1 <= N <= 100,000)
# 입력2) N+1줄까지 각 회의의 시작시간과 끝나는 시간을 공백으로 구분하여 입력한다.
# 시작 시간과 끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0이다.

# 출력 : 최대 사용할 수 있는 회의의 최대 개수를 출력

import sys
sys.stdin = open("input.txt", "r")
n = int(input()) # 회의의 수
time = []

for _ in range(n):
    time.append(list(map(int, input().split())))

time = sorted(time, key=lambda x: x[0])
time = sorted(time, key=lambda x: x[1])

last, cnt = 0, 0
for i, j in time:
    if i >= last:
        cnt += 1
        last = j
print(cnt)