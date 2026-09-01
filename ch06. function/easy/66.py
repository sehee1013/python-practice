# 두 정수를 읽습니다. 예: "10 2" → a=10, b=2
parts = input().split()
num1 = int(parts[0])
num2 = int(parts[1])

# 함수 정의하기
def max_two(num1, num2):
    """두 수 중 큰 값을 반환한다."""
    return num1 if num1 > num2 else num2
    
# max_two.__doc__ 출력
print(max_two.__doc__)
# max_two(num1, num2) 호출 후 출력
print(max_two(num1, num2))