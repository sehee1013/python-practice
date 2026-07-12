# 점수를 tuple 의 첫 자리로 두면 sort 만으로 점수 기준 정렬.
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["X", "Y"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 이름과 점수의 리스트를 동시 순회화며 튜플로 패킹
students = [(score, name) for name, score in zip(names, scores)]

# 패킹한 튜플 리스트를 정렬 후 출력
for score, name in sorted(students):
    print(f"{name}: {score}")