# 함수 정의
def to_seconds(m):
    """분 단위 정수 m을 초로 환산한 값을 반환"""
    return m * 60

m = int(input())

# 함수 호출하여 결과 출력
print(to_seconds(m))