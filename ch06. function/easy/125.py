# 함수 정의하기
def count_kwargs(**kwargs):
    """
    임의의 받은 키워드 인자의 개수를 반환하기

    Args:
        **kwargs (dict)
    Returns:
        int: 받은 키워드 인자 수
    """
    return len(kwargs)

# key=value 토큰을 dict 로 파싱합니다. 예: "a=1 b=2" → opts={"a":"1","b":"2"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(count_kwargs(**opts))