# 1. 함수 정의
# 2. 정수 3개 입력 받기
# 3. 함수 반환값 출력

# 세 수의 합을 반환하는 함수 정의
def sum_three(num1, num2, num3):
    """세 정수를 받아 합 출력"""
    return num1 + num2 + num3

# input().split() 으로 세 칸을 나눠 각각 정수로 바꿉니다. 예: "1 2 3" → num1=1, num2=2, num3=3
num1, num2, num3 = [int(x) for x in input().split()]

# 함수 호출하여 결과 출력
print(sum_three(num1, num2, num3))