data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

# 평균 구하기
average = sum(scores.values()) / len(scores.values())

# 결과 출력
print(f"평균: {average:.1f}")