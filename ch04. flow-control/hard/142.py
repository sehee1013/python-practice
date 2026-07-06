# 빈 다이아몬드를 출력하세요.
n = int(input())

# 가운데 행
center_row = n // 2
first_end_row_empty = (n - 1) // 2

# 가운데 행을 기준으로 삼각형, 역삼각형 출력
print(" " * first_end_row_empty + "*")

# 0행부터 가운데 행 - 1 까지 출력
for row in range(1, center_row):
    
    # 왼쪽 공백: 가운데 행 - row
    left_empty = center_row - row
    # 오른쪽 공백: (row - 1) * 2
    right_empty = (row - 1) * 2 + 1
    
    # 왼쪽 공백, "*", 오른쪽 공백, "*" 출력
    print(" " * left_empty + "*" + " " * right_empty + "*")

# 가운데 행부터 1행까지 - 1 간격으로 출력
for row in range(center_row, 0, -1):
    
    # 왼쪽 공백: 가운데 행 - row
    left_empty = center_row - row
    # 오른쪽 공백: (row - 1) * 2
    right_empty = (row - 1) * 2 + 1
    
    # 왼쪽 공백, "*", 오른쪽 공백, "*" 출력
    print(" " * left_empty + "*" + " " * right_empty + "*")

print(" " * first_end_row_empty + "*")