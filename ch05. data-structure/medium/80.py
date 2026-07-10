students = {
    "윤서": [85, 90, 78],
    "지우": [92, 88, 95],
    "민준": [65, 70],
    "서윤": [80, 80, 80, 80],
}
name = input()

# 입력 받은 name 학생 평균 구하기 -> 출력하기
average = sum(students[name]) / len(students[name])

# 소숫점 1의 자리까지만 출력
print(f"평균: {average:.1f}")