# 위 규칙을 그대로 구현
seed = int(input())

# n1 ~ n6까지 번호 생성
n1 = (seed * 7 + 3) % 45 + 1

# n2: 계산 후 n1과 중복이면 한 번 더 계산
n2 = (n1 * 13 + 11) % 45 + 1

if n2 == n1:
    n2 = n2 % 45 + 1

# n3 ~ n6: 계산 후 앞 번호와 중복이면 최대 2번 번 더 계산
n3 = (n2 * 17 + 7) % 45 + 1

if n3 == n1 or n3 == n2:

    for _ in range(2):
        n3 = n3 % 45 + 1
        if n3 != n1 and n3 != n2:
            break


# n4
n4 = (n3 * 23 + 5) % 45 + 1

if n4 == n1 or n4 == n2 or n4 == n3:

    for _ in range(2):
        n4 = n4 % 45 + 1
        if n4 != n1 and n4 != n2 and n4 != n3:
            break

# n5
n5 = (n4 * 29 + 13) % 45 + 1

if n5 == n1 or n5 == n2 or n5 == n3 or n5 == n4:

    for _ in range(2):
        n5 = n5 % 45 + 1
        if n5 != n1 and n5 != n2 and n5 != n3 and n5 != n4:
            break

# n6
n6 = (n5 * 31 + 17) % 45 + 1

if n6 == n1 or n6 == n2 or n6 == n3 or n6 == n4 or n6 == n5:

    for _ in range(2):
        n6 = n6 % 45 + 1
        if n6 != n1 and n6 != n2 and n6 != n3 and n6 != n4 and n6 != n5:
            break


# 결과 출력
print("=== 로또 번호 ===")
print(f"번호 1: {n1}")
print(f"번호 2: {n2}")
print(f"번호 3: {n3}")
print(f"번호 4: {n4}")
print(f"번호 5: {n5}")
print(f"번호 6: {n6}")
print("행운을 빕니다!")