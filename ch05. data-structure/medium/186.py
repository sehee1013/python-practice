n = int(input())

# 학생 명단 n번 입력 받기
all_students = {input() for _ in range(n)}

# 오늘 출석 인원 입력 받기
m = int(input())

# 출석 명단 m번 입력 받기
attendance_std = {input() for _ in range(m)}

# 결석자 명단 구하기
absent_std = all_students - attendance_std

# 결과 출력
if absent_std:
    print(" ".join(sorted(absent_std)))
else:
    print("전원 출석")