# 세 제곱을 반환하는 함수 정의
def cube(n):
    """정수 n의 세제곱 반환"""
    return n * n * n

# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "2" 이면 n == 2
n = int(input())

# 함수 실행 후 결과 출력
print(cube(n))