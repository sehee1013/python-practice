# 3번 반복하며 계산 결과를 누적하세요.
total = 0

# 3번 입력 받을 때까지 반복
for _ in range(3):
    # 입력 받기
    calculation = input()
    
    # 입력 문자열 공백 구분해서 리스트 저장
    calculation_list = calculation.split(" ")
    
    # 인덱스 0, 2번 정수 변환 
    num1 = int(calculation_list[0])
    num2 = int(calculation_list[2])
    # 인덱스 1번 변수 선언
    operator = calculation_list[1]

    # 인덱스 1번 경우에 따라 계산 후 total에 누적
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        result = num1 // num2
    elif operator == "*":
        result = num1 * num2
    else:
        print("유효한 연산자를 입력하세요.")
        continue
    
    print(result)
    total += result
    
# 합계 출력  
print(f"합계: {total}")