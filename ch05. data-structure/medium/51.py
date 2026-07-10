# zip 으로 두 리스트의 원소를 동시에 받아 컴프리헨션 안에서 사용.
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B"],
    ["solo"],
]
scores_sets = [
    [85, 92, 78, 95, 88],
    [100, 200],
    [42],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 이름과 성적 동시에 받아와서 리스트에 저장
result = [f"{name}={score}" for name, score in zip(names, scores)]

# 결과 출력
print(*result)