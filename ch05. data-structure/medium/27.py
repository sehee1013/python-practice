grid = [
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
r = int(input())

# 리스트에 grid[r] 넣기
result = grid[r]

# 공백 구분으로 출력
print(" ".join(map(str, result)))