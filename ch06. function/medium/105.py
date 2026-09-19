# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 할인율(10), 2개면 둘째 값이 할인율(%)입니다. (정수)
parts = input().split()

# 함수 정의하기
def discount_price(price, rate=10):
    """
    할인 적용 가격을 반환하기

    Args:
        price (int): 할인이 적용될 가격
        rate (int): 할인률 (기본값: 10)
    Returns:
        int: price - (price * rate // 100)
    """
    discount_value = price * rate // 100
    return price - discount_value

# 함수 호출 후 출력
print(discount_price(*map(int, parts)))