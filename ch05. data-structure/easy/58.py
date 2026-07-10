# `a, b = b, a` 한 줄로 임시 변수 없이 두 값을 동시에 교환합니다.
a = int(input())
b = int(input())

print(f"교환 전: a={a} b={b}")

a, b = b, a

# 결과 출력
print(f"교환 후: a={a} b={b}")