# 차/교집합 결과의 길이만 카운트.
s1_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"A", "B", "C"},
    {"X", "Y"},
]
s2_sets = [
    {"지우", "민준", "도윤", "예준", "하준"},
    {"A", "B", "C"},
    {"P", "Q"},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 1학기만 있는 학생
only_1 = s1 - s2
# 2학기만 있는 학생
only_2 = s2 - s1
# 양학기 있는 학생
both = s1 & s2

print(f"1학기만: {len(only_1)}명")
print(f"2학기만: {len(only_2)}명")
print(f"양학기: {len(both)}명")