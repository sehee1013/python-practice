data_sets = [
    [("윤서", 85), ("지우", 92), ("민준", 65), ("서윤", 78), ("도윤", 95)],
    [("A", 70), ("B", 90), ("C", 80)],
    [("solo", 70)],
]
t = int(input())
students = data_sets[t]

top_name = ""
top_score = float('-inf')

# 언패킹으로 이름과 점수 분해
# strict greater로 비교
for name, score in students:
    if score > top_score:
        top_score = score
        top_name = name

# 결과 출력
print(f"{top_name}: {top_score}")    