data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {},
]
t = int(input())
scores = data_sets[t]

# 등록된 학생 수 출력
print(f"총 {len(scores)}명")