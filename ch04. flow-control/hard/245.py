n = int(input())

# n행 출력
for row in range(1, n + 1):
    # row-1개 공백 출력 후 row개 별 출력
    print(" " * (row - 1) + "*" * row)