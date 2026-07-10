students = {
    "윤서": {"수학": 85, "영어": 90, "과학": 78},
    "지우": {"수학": 92, "영어": 88},
    "민준": {"수학": 65, "영어": 70, "과학": 80, "역사": 75},
}
name = input()
subject = input()

# get으로 학생 점수 반환
score = students.get(name, {}).get(subject)

# 점수 없는 경우 "없음" 출력
print(score if score is not None else "없음")