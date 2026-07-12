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
over = []
under = []

# 점수 평균 구하기
average = sum(scores) / len(scores)

# 평균 이상인 학생과 미만인 학생 판별
for name, score in zip(names, scores):
    if score >= average:
        over.append(name)
    else:
        under.append(name)

# 결과 출력
print(f"평균 이상: {' '.join(over)}")
print(f"평균 미만: {' '.join(under)}")