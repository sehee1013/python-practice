# 흐름: 입력 읽기 → difference(num1, num2) 정의 → difference(a, b) 호출 → 결과 출력

# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "10 3" → a=10, b=3
num1, num2 = [int(x) for x in input().split()]

# 함수 정의하기
def difference(num1, num2):
    """num1 - num2 값을 구하여 반환"""
    return num1 - num2

# 함수 호출하여 결과 출력
print(difference(num1, num2))