# 합 계산 후 평균은 합 / 길이.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

# 합 구하기
sum_value = sum(scores.values())
# 평균 구하기
average_value = sum_value / len(scores)

# 결과 출력
print(f"합계: {sum_value}")
print(f"평균: {average_value:.1f}")