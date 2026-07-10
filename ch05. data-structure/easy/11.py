# 정수 리스트를 오름차순 정렬해 공백 구분 한 줄로 출력하세요.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [3, 1, 2],
    [50],
]
t = int(input())
scores = data_sets[t]

# 리스트 오름차순 정렬
scores.sort()

# 결과 출력
print(" ".join(map(str, scores)))