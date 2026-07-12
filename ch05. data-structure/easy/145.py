# strict greater 비교로 첫 본 학생 유지.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

# 가장 큰 점수 구하기
top_score = max(scores.values())

# 가장 큰 점수 가진 첫 학생 구해서 출력하고 종료
for name, score in scores.items():
    if score == top_score:
        print(name)
        break