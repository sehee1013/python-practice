# 한 줄을 공백으로 나눕니다. 첫 토큰=n, 둘째 토큰(있으면)=start. 토큰 1개면 start 는 기본값 1. (정수)
parts = list(map(int, input().split()))

# 함수 정의하기
def range_sum(n, start=1):
    """
    start부터 n까지 정수의 합 반환하기
    
    Args:
        start (int): 시작값
        n (int): 끝값
    Returns:
        start부터 n까지의 정수 합
    """
    total_sum = 0
    for num in range(start, n + 1):
        total_sum += num
    return total_sum

# 함수 호출 후 출력
print(range_sum(*parts))