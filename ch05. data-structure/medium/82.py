data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]
t = int(input())
scores = data_sets[t]

# 추적 변수 선언
top_name = ""
top_score = float('-inf')

# 딕셔너리 순회하며 최고점 학생 찾기
for name, score in scores.items():
    if score > top_score:
        top_score = score
        top_name = name

# 결과 출력
print(f"{top_name}: {top_score}")