# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "4" 이면 n == 4
n = int(input())

# 함수 정의하기
def is_even(n):
    """매개변수 n 을 입력받아, 짝수이면 True, 홀수이면 False 를 반환하기"""
    return n % 2 == 0

# 함수 호출하여 실행 결과 출력
print(is_even(n))