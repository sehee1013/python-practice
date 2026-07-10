# 원본 dict 의 items() 를 순회하면서 if 절로 합격 조건을 검사하세요.
students = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# 점수가 cutoff보다 높은 학생의 점수만 넣은 딕셔너리 생성
cutoff_std = {name: score for name, score in students.items() if score >= cutoff}

# 결과 출력
for name, score in cutoff_std.items():
    print(f"{name}: {score}")