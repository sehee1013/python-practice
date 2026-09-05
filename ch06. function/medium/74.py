# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "5" 이면 n == 5
n = int(input())

# 함수 정의하기
def factorial(n):
    """정수 n의 팩토리얼 값 반환하기"""
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result

# 함수 호출 후 출력
print(factorial(n))