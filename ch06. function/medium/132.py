# 함수 정의하기
def sum_positive_values(**kwargs):
    """
    값이 양수인 것만 더한 합을 반환하기

    Args:
        **kwargs: 임의의 키워드 인자
    Returns:
        int: 양수인 값들의 합
    """
    return sum(value for _, value in kwargs.items() if value > 0)

# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "a=5 b=-3" → opts={"a":5,"b":-3}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(sum_positive_values(**opts))