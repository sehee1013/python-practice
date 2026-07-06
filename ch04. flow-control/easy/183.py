# 가로와 세로를 입력받아 별(*) 사각형을 출력하세요.
width = int(input())
height = int(input())

# 세로 길이만큼 행 출력
for row in range(height):
    print("*" * width)