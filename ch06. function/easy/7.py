# 두 수의 곱을 반환하는 함수 정의
def multiply(num1, num2):
    # num1와 num2 두 수의 곱을 구하여 반환
    return num1 * num2

# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "3 4" → num1=3, num2=4
num1, num2 = [int(x) for x in input().split()]

# 함수 호출하여 결과 출력
print(multiply(num1, num2))