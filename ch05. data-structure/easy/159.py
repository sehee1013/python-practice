s1_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"A", "B", "C"},
    {"X", "Y"},
]
s2_sets = [
    {"지우", "도윤", "예준", "하준"},
    {"A", "B"},
    set(),
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 1학기 - 2학기 차집합으로 1학기만 등록한 학생 색출하고 정렬
only_s1 = sorted(s1 - s2)

# 결과 출력
print(" ".join(only_s1))