# 함수 정의하기
def merge_to_string(**kwargs):
    """
    키를 사전순으로 정렬해 키=값 형태로 , 로 이어 붙인 문자열 반환하기

    Args:
        **kwargs: 임의의 키워드 인자
    Returns:
        str: '키=값' 형식의 문자열
    """
    sorted_kwargs = [f'{key}={value}' for key, value in sorted(kwargs.items())]
    return ",".join(sorted_kwargs)

# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "b=2 a=1" → opts={"b":"2","a":"1"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(merge_to_string(**opts))