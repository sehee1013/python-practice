# 표현식과 if 조건을 함께 사용.
data_sets = [
    [3, -1, 0, 7, -5, 2, -8, 4],
    [10, -5, 20, 0],
    [-1, -2, -3],
]
t = int(input())
data = data_sets[t]

# 리스트 원소 중 양수만 제곱하여 새로운 리스트에 저장
pos_square = [num ** 2 for num in data if num > 0]

# 결과 출력
print(" ".join(map(str, pos_square)))