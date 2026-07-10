# 컴프리헨션 한 줄로 새 리스트를 만든 뒤 출력하세요.
data_sets = [
    [1, 2, 3, 4, 5, 6, 7],
    [10, 20, 30],
    [0],
]
t = int(input())
nums = data_sets[t]

# 제곱수 리스트 생성 후 리스트에 각 원소 제곱 후 추가
nums_square = [num ** 2 for num in nums]

# 결과 출력
print(" ".join(map(str, nums_square)))