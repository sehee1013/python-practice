# 정수 n 을 읽습니다. 예: "5" → n=5
n = int(input())

# 함수 정의하기
def square(n):
    """정수의 제곱을 반환한다."""
    return n * n

# square.__doc__ 출력
print(square.__doc__)
# square(n) 호출 후 출력
print(square(n))