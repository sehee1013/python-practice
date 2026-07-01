# 1부터 50까지 반복
for num in range(1, 51):
    # 15의 배수면 FizzBuzz 출력
    if num % 15 == 0:
        print("FizzBuzz")
    # 3의 배수면 Fizz 출력
    elif num % 3 == 0:
        print("Fizz")
    # 5의 배수면 Buzz 출력
    elif num % 5 == 0:
        print("Buzz")
    # 그 외는 그대로 출력
    else: 
        print(num)