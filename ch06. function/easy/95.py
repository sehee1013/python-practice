# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 지수(2), 2개면 둘째 값이 지수입니다. (값은 정수)
parts = list(map(int, input().split()))

# 함수 정의하기
def power(base, exp=2):
    """
    밑과 지수를 입력받아 base ** exp 를 반환하기
    
    Args:
        base (int): 밑(필수값)
        exp (int): 지수(기본값 = 2)
    Returns:
        base ** exp (int)
    """
    return base ** exp

# 함수 호출 후 출력
print(power(*parts))