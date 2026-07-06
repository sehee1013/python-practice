# 숫자 다이아몬드를 출력하세요.
n = int(input())

# 전략:
#   1. n행 출력
#   2. (n // 2 + 1)행 기준으로 삼각형, 역삼각형 출력.
#   3. i행의 가장 큰 수: i, i를 기준으로 순차 출력, 역순 출력  
center_row = n // 2 + 1

# 첫번째 행부터 삼각형 모양으로 출력
for row in range(1, center_row):
    # 공백: 가운데 행 - 해당 행
    empty = center_row - row
    print(" " * empty, end="")

    # 출력 숫자 해당 행의 숫자까지만 증가, 이후엔 감소 
    for i in range(1, row):
        print(i, end="")
    for i in range(row, 0, -1):
        print(i, end="")
    print()

# 가운데 행부터 역삼각형 모양으로 출력
for row in range(center_row, 0, -1):
    empty = center_row - row
    print(" " * empty, end="")

    # 출력 숫자 해당 행의 숫자까지만 증가, 이후엔 감소 
    for i in range(1, row):
        print(i, end="")
    for i in range(row, 0, -1):
        print(i, end="")
    print()