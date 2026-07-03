score = int(input())

# 등급 변수 선언
grade = ""

# 입력 받은 점수 90점 이상이면 A
if score >= 90:
    grade += "A"
# 입력 받은 점수 80점 이상이면 B
elif score >= 80:
    grade += "B"
# 입력 받은 점수 70점 이상이면 C
elif score >= 70:
    grade += "C"
# 입력 받은 점수 60점 이상이면 D
elif score >= 60:
    grade += "D"
# 입력 받은 점수 60점 미만이면 F
else:
    grade += "F"

# 점수, 등급 출력
print(f"점수: {score}\n등급: {grade}")