# N을 두 소수의 합으로 표현하는 모든 경우를 출력하세요.
N = int(input())
prime_nums = []

# n까지 순회하며 소수 리스트에 넣기
for num in range(2, N):
    prime = True
    # 1과 본인 이외에 나누어 떨어지는 수는 소수 아님
    for divisor in range(2, num):
        if num % divisor == 0:
            prime = False
            break
    # 소수만 리스트 추가
    if prime:
        prime_nums.append(num)

# 리스트 중 2개의 수를 더했을 때 n이 되면 출력
for prime_num1 in prime_nums:
    for prime_num2 in prime_nums:
        # 앞에 수가 뒤에 수보다 작아야 함
        if prime_num1 + prime_num2 == N and prime_num1 <= prime_num2:
            print(f"{N} = {prime_num1} + {prime_num2}")