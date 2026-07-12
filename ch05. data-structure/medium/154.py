data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]


# 각각의 성적을 순회
for name, score in scores.items():
    rank = 1

    # 다른 성적과 비교하여 더 높은 성적이 있으면 + 1
    for _, other_score in scores.items():
        if other_score > score:
            rank += 1
            
    # 결과 출력
    print(f"{name}: {rank}등")