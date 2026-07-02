# 2부터 N까지 완전수를 찾아 출력하세요.
n = int(input())

# 2부터 정수 N까지 반복
for i in range(2, n + 1):
    divisors = []

    # 약수 구하기
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            divisors.append(j)
            # 중복 및 자기 자신 제외
            if j != i // j and i != i // j:
                divisors.append(i // j)
    
    divisors.sort() #오름차순 정렬

    # 정수의 모든 약수를 더한 값이 정수 값과 같으면 출력    
    if i == sum(divisors):
        print(f'{i} = {" + ".join(map(str, divisors))}')