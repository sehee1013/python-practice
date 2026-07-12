# 두 평균 비교 후 셋 중 하나 출력.
s1_sets = [
    {"윤서": 85, "지우": 92, "민준": 65},
    {"A": 90, "B": 90},
    {"X": 80, "Y": 80},
]
s2_sets = [
    {"지우": 88, "민준": 70, "도윤": 95},
    {"C": 70, "D": 80},
    {"P": 80, "Q": 80},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 각 학기 평균 구하기
s1_average = sum(s1.values()) / len(s1)
s2_average = sum(s2.values()) / len(s2)

# 각 학기 평균 출력
print(f"1학기 평균: {s1_average:.1f}")
print(f"2학기 평균: {s2_average:.1f}")

# 둘 중 더 높은 학기 구해서 출력
if s1_average > s2_average:
    winner = "1학기"
elif s1_average < s2_average:
    winner = "2학기"
else:
    winner = "무승부"

print(f"승: {winner}")