# 3자리 정수를 입력받아 각 자리를 분해하고 합, 곱을 출력하세요.
num = int(input())

# 각 자릿수를 구하기
# 100의 자리
digit_100s = num // 100
num %= 100

# 10의 자리
digit_10s = num // 10

# 1의 자리
digit_1s = num % 10

# 각 자릿수 출력
print(f"백의자리: {digit_100s}")
print(f"십의자리: {digit_10s}")
print(f"일의자리: {digit_1s}")

# 합 출력
print(f"합: {digit_100s + digit_10s + digit_1s}")
# 곱 출력
print(f"곱: {digit_100s * digit_10s * digit_1s}")