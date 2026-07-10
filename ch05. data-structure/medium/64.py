# zip 은 짧은 쪽 길이까지만 짝지어 줍니다.
names_sets = [
    ["A", "B", "C", "D", "E"],
    ["윤서", "지우", "민준"],
    ["solo"],
]
scores_sets = [
    [85, 92, 78],
    [85, 92, 65],
    [42],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 두 리스트 묶어서 (이름, 점수) tuple 생성 후 출력
for name, score in zip(names, scores):
    print(f"{name}: {score}")