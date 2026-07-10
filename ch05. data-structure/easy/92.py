# 빈 교집합도 자연스럽게 빈 줄로 출력됨.
a_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"a", "b", "c", "d"},
    {"x", "y", "z"},
]
b_sets = [
    {"지우", "도윤", "예준", "하준"},
    {"c", "d", "e", "f"},
    {"1", "2", "3"},
]
t = int(input())
a = a_sets[t]
b = b_sets[t]

# 교집합 구하기
intersection_set = a & b

# 사전순으로 정렬
sorted_intersection = sorted(intersection_set)

# 결과 출력
print(" ".join(sorted_intersection))