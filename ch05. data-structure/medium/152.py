data_sets = [
    {
        "윤서": {"수학": 85, "영어": 90, "과학": 78},
        "지우": {"수학": 92, "영어": 88, "과학": 95},
        "민준": {"수학": 65, "영어": 70, "과학": 80},
    },
    {
        "A": {"수학": 90, "영어": 80},
        "B": {"수학": 70, "영어": 80},
    },
    {
        "혼자": {"수학": 80},
    },
]
t = int(input())
students = data_sets[t]

# 각 학생의 평균 구해서 딕셔너리 생성
for name, subs in students.items():
    average = sum(subs.values()) / len(subs.values())
    
    # 결과 출력
    print(f"{name}: {average:.1f}")