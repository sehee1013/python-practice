# 직장인 여부 → 연봉 → 신용등급 → 연봉 재검사 순서로 if를 중첩하세요.
is_employed = input() == "True"
salary = int(input())
credit_grade = int(input())

# 직장인이 아닌 경우
if not is_employed:
    print("직장인 확인 필요")
else:
    # 연봉 3000만원 미만인 경우
    if salary < 3000:
        print("연봉 조건 미달")
    else:
        # 신용등급 3등급 이하인 경우
        if credit_grade <= 3:
            print("대출 한도: 5000만원")
        else:
            # 연봉 5000만원 이상인 경우
            if salary >= 5000:
                print("대출 한도: 3000만원")
            else:
                print("대출 한도: 1000만원")