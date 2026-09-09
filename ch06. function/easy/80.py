# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "3 5" → num1=3, num2=5
num1, num2 = [int(x) for x in input().split()]

# 함수 정의하기
def sum_product(num1, num2):
    """두 정수 num1, num2의 합과 곱을 반환하기"""
    return num1 + num2, num1 * num2

# 함수 호출 후 결과 언패킹하기
sum_num1_num2, product_num1_num2 = sum_product(num1, num2)
# 결과 출력하기
print(sum_num1_num2, product_num1_num2)