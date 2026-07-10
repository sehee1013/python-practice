# (점수, 이름) tuple 의 자연스러운 정렬을 활용하세요.
data_sets = [
    [(85, "윤서"), (92, "지우"), (65, "민준"), (78, "서윤"), (95, "도윤")],
    [(80, "A"), (70, "B"), (90, "C")],
    [(50, "혼자")],
]
t = int(input())
students = data_sets[t]

# 점수 오름차순으로 정렬해 출력
# 오름차순 정렬
students.sort()


# 이름과 점수 각각 언패킹 후 결과 출력
for score, name in students:
    print(f"{name}: {score}")