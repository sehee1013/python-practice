# 빈 리스트에서 시작해 N번 입력을 받아 append로 추가하세요. 출력 시 join을 활용하면 깔끔합니다.
n = int(input())
attendance_list = []

# 학생 이름 n번 입력 받을 때까지 반복
for _ in range(n):

    # 학생 이름 입력
    name = input()

    # 이름 리스트 추가
    attendance_list.append(name)

# 출석 인원수와 명단 출력
print(f"출석 {n}명")
print("명단: " + " ".join(attendance_list))