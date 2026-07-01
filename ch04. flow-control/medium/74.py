height = float(input())
weight = float(input())
age = int(input())
bmi_level = ""

#bmi 계산
bmi = weight / (height / 100) ** 2

# 나이대 별 판정 등급 분류 후 bmi와 함께 출력
if age >= 20:
    if bmi < 18.5:
        bmi_level = "저체중"
    elif bmi < 23:
        bmi_level = "정상"
    elif bmi < 25:
        bmi_level = "과체중"
    else:
        bmi_level = "비만"

if age < 20:
    if bmi < 17:
        bmi_level = "저체중 (청소년 기준)"
    elif bmi < 23:
        bmi_level = "정상 (청소년 기준)"
    else:
        bmi_level = "과체중 주의 (청소년 기준)"

print(f"BMI: {round(bmi, 2)}")
print(f"판정: {bmi_level}")