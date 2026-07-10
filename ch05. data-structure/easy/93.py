a_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"a", "b", "c", "d"},
    {"x", "y"},
]
b_sets = [
    {"지우", "도윤", "예준"},
    {"c", "d", "e"},
    {"x", "y", "z"},
]
t = int(input())
a = a_sets[t]
b = b_sets[t]

# 차집합 구하기
difference_set = a - b

# 사전적으로 정렬하여 조건 부합 시키기
sorted_result = sorted(difference_set)

# 공백 구분자 주고 한 줄 출력
print(" ".join(sorted_result))