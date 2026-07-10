# 각 그룹 list 를 빌딩 후 빈 경우 라벨만 출력.
s1_sets = [
    {"윤서": 85, "지우": 92, "민준": 65},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50},
]
s2_sets = [
    {"지우": 88, "민준": 70, "도윤": 95, "예준": 60},
    {"A": 85, "B": 95, "C": 75},
    {"Y": 60},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

both = []
only1 = []
only2 = []

# s1과 s2 둘 다 있는 경우
for key in s1:
    if key in s2:
        both.append(key)

    # s1에만 있는 경우
    else:
        only1.append(key)

# s2에만 있는 경우
for key in s2:
    if key not in s1:
        only2.append(key)

# 결과 출력
print("1학기만:", " ".join(only1))
print("2학기만:", " ".join(only2))
print("양학기:", " ".join(both))