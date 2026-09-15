# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 증가폭(1), 2개면 둘째 값이 증가폭입니다. (정수)
parts = list(map(int, input().split()))

# 함수 정의하기
def increment(n, step=1):
    """
    n + step을 반환하기

    Args:
        n (int): 증가시킬 정수
        step (int): 증가폭(기본값 1)
    Returns:
        int: n + step
    """
    return n + step

# 함수 호출 후 출력
print(increment(*parts))