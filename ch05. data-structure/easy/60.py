points = [(1, 2), (3, 4), (5, 6), (7, 8), (-1, -2)]
n = int(input())

# n번째 tuple의 좌표 구하기
x, y = points[n-1]

# 결과 출력
print(f"x: {x}")
print(f"y: {y}")