# 두 통계를 따로 계산해 두 줄 출력.
s1_sets = [
    {"윤서": 85, "지우": 92, "민준": 65},
    {"A": 70, "B": 80},
    {"X": 70},
]
s2_sets = [
    {"지우": 88, "민준": 70, "도윤": 95},
    {"A": 90, "B": 80},
    {"X": 70},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]


# 전체 평균 구하기
all_score = list(s1.values()) + list(s2.values())
all_average = sum(all_score) / len(all_score)


# 양학기 등록한 학생들의 2학기 평균 구하기
both = set(s1.keys()) & set(s2.keys())

# 학생들 순회하며 점수 합산하여 평균 구하기
average2 = sum(s2[name] for name in both) / len(both)

# 결과 출력
print(f"전체 평균: {all_average:.1f}")
print(f"양학기 2학기 평균: {average2:.1f}")