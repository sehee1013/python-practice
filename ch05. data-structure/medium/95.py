s1_sets = [
    {"윤서", "지우", "민준"},
    {"A", "B", "C"},
    {"X", "Y"},
]
s2_sets = [
    {"지우", "민준", "도윤", "예준"},
    {"A", "B", "C"},
    {"P", "Q"},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 1학기만 듣는 경우
only1 = s1 - s2

# 2학기만 듣는 경우
only2 = s2 - s1

# 모두 듣는 경우
both = s1 & s2

# 결과 출력
print("1학기만:", " ".join(sorted(only1)))
print("2학기만:", " ".join(sorted(only2)))
print("양학기:", " ".join(sorted(both)))