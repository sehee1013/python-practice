# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "17 5" → num1=17, num2=5
num1, num2 = [int(x) for x in input().split()]

# 함수 정의하기
def divide(num1, num2):
    """정수 num1를 정수 num2로 나눈 몫과 나머지를 함께 반환하기"""
    return num1 // num2, num1 % num2

# 몫과 나머지 언패킹
quotient, remainder = divide(num1, num2)

# 몫과 나머지 출력
print(quotient, remainder)