num1 = float(input())
op = input()
num2 = float(input())

# 전략: 입력받은 연산자에 맞는 연산 결과 출력
if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    # num2가 0인 경우 나눗셈 연산 불가 메시지 출력
    if num2 == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
# 지원하지 않는 연산자 입력 시 경고 메시지 출력
else:
    print("지원하지 않는 연산자입니다.")