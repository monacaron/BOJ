# 220530
# 패션왕 신해빈
# 한 번 입었던 옷들의 조합 중복 x
# 의상들이 주어졌을 때 최대 몇 개의 조합이 가능한지 구하는 프로그램

# 입력1) 테스트 케이스 개수 T. 최대 100개
# 입력2) 의상의 수 n (0 <= n <= 30)
# 입력3) n줄에 걸쳐 가진 의상의 이름과 종류가 공백으로 구분되어 주어짐. 같은 종류의 의상은 하나만 입을 수 있음.
# 모든 문자열은 1 이상 20 이하의 알파벳 소문자로 이루어져있으며, 같은 이름을 가진 의상 x

# 출력 : 최대 조합 개수

# a, b, c 타입의 의상이 있다면 ~ result = (a + 1) * (b + 1) * (c + 1) - 1
# +1 : 해당 타입의 옷을 안입는 경우를 더하는 것
# -1 : 아무것도 착용하지 않은 경우를 빼주는 것
import sys
sys.stdin = open("input.txt", "r")

t = int(input()) # 테스트 케이스 개수

for test_case in range(1, t + 1):
    n = int(input()) # 의상의 수

    clothes = {}
    for _ in range(n):
        x, y= map(str, input().split())
        if y in clothes:
            clothes[y].append(x)
        else:
            clothes[y] = [x]

    result = 1
    for i in clothes:
        result *= len(clothes[i]) + 1
    print(result - 1)