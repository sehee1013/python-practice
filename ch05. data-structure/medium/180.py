n = int(input())
students = []

# n번 이름, 학번 형식으로 입력 받기
for _ in range(n):
    name, student_id = input().split(',')
    students.append((int(student_id), name))

# 학번은 정수로 변환하여 오름차순 정렬
sorted_pairs = sorted(students)

# 학번: 이름 형식으로 결과 출력
for student_id, name in sorted_pairs:
    print(f"{student_id}: {name}")