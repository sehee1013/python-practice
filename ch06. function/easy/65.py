# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "3 3" → a=3, b=3
num1, num2 = [int(x) for x in input().split()]

# 함수 정의하기
def is_equal(num1, num2):
    """두 정수가 같은지 판별한다"""
    if num1 == num2:
        return True
    return False

# 함수 호출 후 출력
print(is_equal(num1, num2))