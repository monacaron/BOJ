# 220530
# 다리 놓기
# 강의 서쪽에는 N개의 사이트가 있고, 동쪽에는 M개의 사이트가 있다.(N <= M)
# 서쪽의 사이트와 동쪽의 사이트를 다리로 연결한다.
# 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼(N개) 다리를 지으려고 한다.
# 다리끼리는 서로 겹쳐질 수 없다고 할 때, 다리를 지을 수 있는 경우의 수를 구하는 프로그램

# 입력1) 테스트 케이스 개수 T
# 입력2) 서쪽 사이트 개수 N, 동쪽 사이트 개수 M (0 < N <= M < 30)

# 출력 : 주어진 조건 하에 다리를 지을 수 있는 경우의 수

# M개 중 N개 고르기 ~ M개 중 M-N개 고르기
# M! / N!(M-N)!
def facto(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * facto(x - 1)
t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    result = facto(m) // (facto(n) * facto(m-n))

    print(result)