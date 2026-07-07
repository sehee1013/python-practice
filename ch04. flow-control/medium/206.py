# 구간 내 소수를 찾아 출력
start = int(input())
end = int(input())

# 소수 리스트 생성
primes = []

# 입력 받은 숫자 사이에서 반복
for num in range(start, end + 1):

    # 2 미만인 수는 넘어감
    if num < 2:
        continue

    # 소수 플래그
    is_prime = True
    
    # 1부터 num까지 숫자 반복 -> 소수 판별
    for i in range(2, num):
        # num % i == 0이면 소수 아님
        if num % i == 0:
            is_prime = False
            break

    # 소수면 리스트에 추가
    if is_prime:
        primes.append(num)

# 결과 출력
print(" ".join(map(str, primes)))