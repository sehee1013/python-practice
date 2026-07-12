data_sets = [
    [85, 92, 65, 85, 95, 92, 78, 65],
    [1, 2, 3, 1, 2],
    [100, 100, 100],
]
t = int(input())
scores = data_sets[t]

# 중복 제거 후 오름차순으로 정렬
sorted_scores = sorted(set(scores))

# str로 변환 후 공백 구분하여 한 줄 출력
print(" ".join(map(str, sorted_scores)))