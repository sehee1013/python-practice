# 두 수의 GCD와 LCM을 출력하세요.
a = int(input())
b = int(input())

origin_a = a
origin_b = b

# 최대공약수 구하기
# b가 0이 될 때까지 반복
while b != 0:
    # 유클리드 호제법
    a, b = b, a % b

gcd = a

# 최소 공배수 구하기
lcm = origin_a * origin_b // gcd

# 결과 출력
print(f"최대공약수(GCD): {gcd}")
print(f"최소공배수(LCM): {lcm}")