# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 수량(1), 2개면 둘째 값이 수량입니다. (정수)
parts = list(map(int, input().split()))

# 함수 정의하기
def total_price(unit_price, count=1):
    """
    unit_price * count를 반환하기

    Args:
        unit_price (int): 단가
        count (int): 수량
    Returns:
        int: unit_price * count
    """
    return unit_price * count

# 함수 호출 후 출력
print(total_price(*parts))