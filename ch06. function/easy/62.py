# 두 정수를 읽습니다. 예: "3 5" → a=3, b=5
parts = input().split()
num1 = int(parts[0])
num2 = int(parts[1])

# 함수 정의하기
def add(num1, num2):
    """두 정수의 합을 반환한다."""
    return num1 + num2

# add.__doc__ 출력
print(add.__doc__)
# add(num1, num2) 호출 후 출력
print(add(num1, num2))