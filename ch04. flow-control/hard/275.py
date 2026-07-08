is_employed = input() == "True"
salary = int(input())
credit_grade = int(input())

# 직장인이 아니면 직장인 확연 필요
if not is_employed:
    print("직장인 확인 필요") 

# 연봉 3000만원 미만이면 연봉 조건 미달
elif salary < 3000:
    print("연봉 조건 미달")

# 연봉 5000만원 미만, 신용등급 4등급 이상 대출한도 1000
elif salary < 5000 and credit_grade >= 4:
    print("대출 한도: 1000만원")

# 연봉 5000만원 이상, 신용등급 4등급 이상 대출 한도 3000만원
elif salary >= 5000 and credit_grade >= 4:
    print("대출 한도: 3000만원")
    
# 신용등급 3등급 이하면 대출 한도 5000만원
else:
    print("대출 한도: 5000만원")