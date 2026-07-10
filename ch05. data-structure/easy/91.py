# 출력 시 set 을 정렬해 일관된 순서로 표시.
a_sets = [
    {"윤서", "지우", "민준"},
    {"a", "b", "c"},
    {"1", "2", "3"},
]
b_sets = [
    {"지우", "도윤", "예준"},
    {"x", "y", "z"},
    set(),
]
t = int(input())
a = a_sets[t]
b = b_sets[t]

# 합집합 구하기
union_set = a | b

# 사전순으로 정렬
sorted_union = sorted(union_set)

# 결과 출력
print(" ".join(sorted_union))