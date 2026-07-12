# set 으로 중복 제거 + 정렬 + 출력.
data_sets = [
    ["윤서", "지우", "민준", "윤서", "도윤", "지우", "예준"],
    ["A", "B", "C"],
    ["혼자", "혼자", "혼자"],
]
t = int(input())
names = data_sets[t]

# 현재 리스트 중복 제거 후 요소 개수 출력
set_names = set(names)
print(f"총 {len(set_names)}명")

# 리스트 정렬 후 언패킹 출력
print(*sorted(set_names))