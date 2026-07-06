# 숫자와 N을 입력받아 2~N의 배수인지 각각 출력하세요.
num = int(input())
n = int(input())

# n까지 순회하기
for divisor in range(2, n + 1):
    # num을 n으로 딱 나누어 떨어지면 배수
    if num % divisor == 0:
        print(f"{divisor}의 배수입니다.")
    # 나누어 떨어지지 않으면 배수 아님
    else:
        print(f"{divisor}의 배수가 아닙니다.")