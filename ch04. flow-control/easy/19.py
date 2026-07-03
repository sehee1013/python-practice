# cm를 m로 변환한 후 BMI = weight / (height_m ** 2). round(bmi, 2) 사용.
height = float(input())
weight = float(input())
# bmi 변수에 공식 넣기
bmi = weight / (height / 100) ** 2 

# bmi 값이 18.5 미만이면 저체중 
if bmi < 18.5:
    judgment = "저체중"
# bmi 값이 18.5 이상, 23 미만이면 정상 
elif bmi < 23:
    judgment = "정상"  
# bmi 값이 23이상, 25미만이면 과제충 
elif bmi < 25:
    judgment = "과체중"
# bmi 값이 25 이상이면 비만 
else:
    judgment = "비만"

print(f"키: {height}cm, 몸무게: {weight}kg")
print(f"BMI: {round(bmi, 2)}")
print(f"판정: {judgment}")