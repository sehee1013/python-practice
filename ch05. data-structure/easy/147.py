# items() 로 (이름, 점수) 동시 받아 등급 분기.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

# 리스트 순회하며 각 성적을 기준에 따라 등급 판별
for name, score in scores.items():
    if score >= 90:
        rank = "A"
    elif score >= 80:
        rank = "B"
    elif score >= 70:
        rank = "C"
    elif score >= 60:
        rank = "D"
    else:
        rank = "F"

    # 결과 출력
    print(f"{name}: {rank}")