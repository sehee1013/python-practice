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

# 이름과 점수 zip해서 순회
for name, score in zip(names, scores):
    rank = 1

    # 다른 학생들의 점수와 비교하여 높은 성적인 학생이 있을 때마다 + 1
    for other_score in scores:
        if other_score > score:
            rank += 1
            
    # 결과 출력
    print(f"{name}: {rank}등")