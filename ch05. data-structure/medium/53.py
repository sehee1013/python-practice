n = int(input())

# x값과 x의 제곱 값을 넣은 딕셔너리 생성
square_table = {num: num * num for num in range(1, n + 1)}

# 결과 출력
for num, square in square_table.items():
    print(f"{num}: {square}")