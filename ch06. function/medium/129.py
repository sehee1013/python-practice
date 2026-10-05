# 함수 정의하기
def max_value_key(**kwargs):
    """
    임의의 키워드 인자를 받아, 값이 가장 큰 항목의 키 이름 반환하기

    Args:
        **kwargs: 임의의 키워드 인자
    Returns:
        str: 값이 가장 큰 항목의 키 이름
    """
    new_list = [(value, key) for key, value in kwargs.items()]
    sorted_new_list = sorted(new_list, reverse=True)
    return sorted_new_list[0][1]

# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "a=3 b=7" → opts={"a":3,"b":7}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(max_value_key(**opts))