# 1부터 N 사이의 쌍둥이 소수 쌍을 출력하세요.
n = int(input())
prime_set = set()

# 1부터 N 사이의 소수 구하기
for num in range(2, n + 1):

    # 약수 플래그
    is_prime_num = True

    for i in range(2, num):

        # 약수가 있으면 약수 아님. 즉시 종료
        if num % i == 0:
            is_prime_num = False
            break

    # 소수인 것만 set 저장
    if is_prime_num:
        prime_set.add(num)
        
        # 소수 - 2가 약수 리스트에 있으면 같이 출력
        if num - 2 in prime_set:
            print(f"({num - 2}, {num})")