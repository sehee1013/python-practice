# 점수가 동률인 경우 이름 알파벳순으로 자동 정렬됨.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"A": 50, "B": 50, "C": 50},
]
t = int(input())
scores = data_sets[t]

# 튜플 리스트로 변환
score_std = [(score, name) for name, score in scores.items()]

# 점수 기준으로 정렬
sorted_score_std = sorted(score_std)

# 순회하여 결과 출력
for score, name in sorted_score_std:
    print(f"{name}: {score}" )