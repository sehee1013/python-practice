# 누진세율: 구간별로 나누어 계산하세요
salary = int(input())
total_duty = 0

SECTION1 = 1200
SECTION2 = 4600

# 구간별 세율 판별하여 적용
if salary <= SECTION1:
    total_duty += salary * 0.06

elif salary <= SECTION2:
    total_duty += SECTION1 * 0.06
    total_duty += (salary - SECTION1) * 0.15
else:
    total_duty += SECTION1 * 0.06
    total_duty += (SECTION2 - SECTION1) * 0.15
    total_duty += (salary - SECTION2) * 0.24

# 결과 출력
print(f"연봉: {salary}만원")
print(f"세금: {round(total_duty)}만원")