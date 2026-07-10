data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]
t = int(input())
scores = data_sets[t]
scores_value = scores.values()

total = sum(scores_value)

# 합계 출력
print(f"합계: {total}")
# 평균 구해서 출력
average = total / len(scores_value)
print(f"평균: {average:.1f}")
# 최고값 구해서 출력
print(f"최고: {max(scores_value)}")
# 최저값 구해서 출력
print(f"최저: {min(scores_value)}")