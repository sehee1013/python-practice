# 1부터 N 사이의 해밍수를 출력하세요.
N = int(input())

# n이 1이 될 때까지 2, 3, 5로 나누어 떨어지지 않으면 해밍수 아님
for num in range(1, N + 1):
    hamming = True
    original_num = num

    # num이 1보다 큰 동안 2, 3, 5로 나누어 떨어지는지 검사하여 해밍수 판별
    while num > 1:
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            hamming = False
            break

        # num 갱신해주기
        if num % 2 == 0:
            num //= 2
        elif num % 3 == 0:
            num //= 3
        elif num % 5 == 0:
            num //= 5

    # 해밍수면 출력
    if hamming:
        print(original_num)