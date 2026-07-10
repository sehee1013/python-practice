a_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"A", "B", "C"},
    {"X", "Y", "Z"},
]
b_sets = [
    {"지우", "도윤", "예준", "하준"},
    {"A", "B", "C"},
    set(),
]
t = int(input())
a = a_sets[t]
b = b_sets[t]

# 한쪽에만 있는 원소 (차집합)를 정렬해 공백 구분하여 한 줄에 출력하기
# 교집합 구해서 합집합에서 빼기
sym_diff = (a | b) - (a & b)

# 정렬하여 공백 구분으로 결과 출력
print(" ".join(sorted(sym_diff)))