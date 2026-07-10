# `reverse=True` 인자가 핵심입니다.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [3, 1, 2],
    [50],
]
t = int(input())
scores = data_sets[t]

# 리스트 내림차순 정렬하고 리스트에 대입
scores = sorted(scores, reverse=True)

# 결과 출력
print(" ".join(map(str, scores)))