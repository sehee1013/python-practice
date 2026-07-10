# `for name, score in students:` 형태로 각 tuple을 두 변수로 한 번에 받아 순회하세요.
students = [
    ("윤서", 85),
    ("지우", 92),
    ("민준", 65),
    ("서윤", 78),
    ("도윤", 95),
]
target = input()
found = False

for name, score in students:
    # 학생이 있으면 점수 출력
    if target == name:
        print("점수:", score)
        found = True
    
# 없으면 없음 메시지 출력
if not found:
    print("학생 없음")    