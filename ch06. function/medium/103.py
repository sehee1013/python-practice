# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 low, high 가 기본값으로 채워집니다. (모두 정수)
parts = list(map(int, input().split()))

# 함수 정의하기
def clamp(value, low=0, high=100):
    """
    value를 [low, high] 범위로 제한한 값을 반환하기

    Args:
        value (int): 정수
        low (int): 하한 (기본값: 0)
        high (int): 상한 (기본값: 100)
    Returns:
        int: [low, high] 범위로 제한한 값
    """
    return max(low, min(high, value))

# 함수 호출 후 출력
print(clamp(*parts))