# 가운데 정렬된 별 피라미드를 출력
n = int(input())

# n행만큼 출력, i번째 행: (n - row)개 공백 출력 후 (2*row-1)개의 별 출력
for row in range(1, n + 1):
    print(" " * (n - row) + "*" * (2 * row - 1))