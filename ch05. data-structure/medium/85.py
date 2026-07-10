data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95, "예준": 50},
    {"A": 78, "B": 95, "C": 55},
    {"윤서": 100, "지우": 95, "민준": 90},
]
t = int(input())
scores = data_sets[t]

# 등급별 리스트 생성
grade_a = []
grade_b = []
grade_c = []
grade_f = []

# 점수에 따라 리스트 추가
for name, score in scores.items():
    if score >= 90:
        grade_a.append(name)
    elif score >= 80:
        grade_b.append(name)
    elif score >= 70:
        grade_c.append(name)
    else:
        grade_f.append(name)
        
# 결과 출력
print(f"A: {' '.join(grade_a)}")
print(f"B: {' '.join(grade_b)}")
print(f"C: {' '.join(grade_c)}")
print(f"F: {' '.join(grade_f)}")