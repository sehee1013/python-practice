main_sets = [
    {"수학": 80, "영어": 75, "과학": 90},
    {"A": 1, "B": 2},
    {"X": 10, "Y": 20},
]
update_sets = [
    {"영어": 88, "역사": 70},
    {"C": 3, "D": 4},
    {},
]
t = int(input())
main = main_sets[t]
update_data = update_sets[t]

# main 복사 후 update_data 업데이트
merged = main.copy()
merged.update(update_data)

# 결과 출력
for subject, score in merged.items():
    print(f"{subject}: {score}")