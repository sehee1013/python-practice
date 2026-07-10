positions = {
    (0, 0): 'A',
    (0, 1): 'B',
    (1, 0): 'C',
    (2, 3): 'X',
    (4, 4): 'GOAL',
}
row = int(input())
col = int(input())

# 입력한 좌표가 딕셔너리에 있는 경우 키값 출력, 없으면 없음 출력
print(positions.get((row, col), "없음"))