# 2부터 N까지 각 수가 소수인지 판별하여 출력하세요.
n = int(input())
total_prime_nums = 0

# 2부터 입력 받은 값 사이에 있는 모든 소수를 한 줄에 공백으로 시각적 구분하여 출력
for i in range(2, n + 1):
    is_prime = True

    for j in range(2, int(i ** 0.5 + 1)):
        if i % j == 0:
            is_prime = False
            break
    else: 
        total_prime_nums += 1
        print(i, end=" ")

print(f"\n소수 개수: {total_prime_nums}")