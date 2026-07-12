s1_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "도윤": 88},
    {"A": 70, "B": 80},
    {"X": 90},
]
s2_sets = [
    {"지우": 88, "민준": 70, "도윤": 95, "예준": 60},
    {"A": 80, "B": 70},
    {"X": 90},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

total_score = 0

# 공통 학생 집합 구하기
both = set(s1.keys()) & set(s2.keys())

# 공통 학생의 양 학기 성적 합 구하기
for name in both:
    total_score += s1[name] + s2[name]

# 평균 구하기
average = total_score / (len(both) * 2)

# 결과 출력
print(f"양 학기 학생 평균: {average:.1f}")