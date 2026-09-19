# 함수 정의하기
def price_with_options(base, tax=10, ship=0):
    """
    base와 tax, ship을 입력받아 결제 금액을 반환하기

    Args: 
        base (int): 세율이 적용되지 않은 기본가
        tax (int): 세율 (기본값: 10)
        ship (int): 배송비 (기본값: 0)
    Returns:
        int: base + base * tax // 100 + ship
    """
    return base + base * tax // 100 + ship

# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 tax, ship 이 기본값으로 채워집니다. (모두 정수)
parts = input().split()

# 함수 호출 후 출력
print(price_with_options(*map(int, parts)))