# 함수 정의하기
def average_values(**kwargs):
    """
    값들의 평균을 반환하기

    Args:
        **kwargs: 임의의 키워드 인자
    Returns:
        int: 값들의 평균
    """
    return sum(kwargs.values()) // len(kwargs.keys())

# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "a=2 b=4 c=6" → opts={"a":2,"b":4,"c":6}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(average_values(**opts))