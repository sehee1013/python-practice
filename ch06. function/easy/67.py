# input().split() 으로 세 칸을 나눠 각각 정수로 바꿉니다. 예: "1 2 3" → a=1, b=2, c=3
num1, num2, num3 = [int(x) for x in input().split()]

# 함수 정의하기
def max_three(num1, num2, num3):
    """세 정수 중 가장 큰 값을 반환하기"""
    return max(num1, num2, num3)

# 함수 호출 후 출력
print(max_three(num1, num2, num3))