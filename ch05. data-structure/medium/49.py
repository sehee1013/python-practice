# 한 줄에 두 개의 for 를 두는 이중 컴프리헨션을 사용하세요.
grids = [
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
    [[1, 2, 3], [4, 5, 6]],
    [[1], [2], [3]],
]
t = int(input())
grid = grids[t]

# 큰 리스트 속 요소 리스트의 요소값 차례대로 입력
result = [num for row in grid for num in row]

# 결과 출력
print(*result)