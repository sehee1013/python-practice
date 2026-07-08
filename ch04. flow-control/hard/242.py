# N*N 사각형에서 테두리와 대각선만 별로 출력
n = int(input())

# 행과 열의 테두리, 대각선이면 "*" 출력. 그 외: " " 출력
for row in range(n):
    print("".join('*' if (row == col or row + col == n - 1 or row == 0 or row == n - 1 or col == 0 or col == n - 1) else ' ' for col in range(n)))