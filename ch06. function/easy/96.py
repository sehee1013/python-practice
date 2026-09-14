# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 할인(0), 2개면 둘째 값이 할인액입니다. (값은 정수)
parts = list(map(int, input().split()))

# 함수 정의하기
def final_price(price, discount=0):
    """
    price와 discount를 입력받아 price - discount를 반환하기
    
    Args:
        price (int): 가격
        discount (int): 할인액
    Returns:
        int: 할인 적용 최종 가격
    """
    return price - discount

# 함수 호출 후 출력
print(final_price(*parts))