data_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤", "예준"],
    ["red", "green", "blue"],
    ["혼자"],
]
t = int(input())
names = data_sets[t]

# data_sets[t]의 첫번째, 마지막 이름 출력
print(f"첫 번째: {names[0]}")
print(f"마지막: {names[-1]}")