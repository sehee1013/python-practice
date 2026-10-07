# 함수 정의하기
def longest_value(**kwargs):
    """
    값 중 가장 긴 것을 반환하기

    Args:
        **kwargs: 임의의 키워드 인자
    Returns:
        str: 가장 긴 것
    """
    longest_word = ""
    for key, value in kwargs.items():
        if len(value) > len(longest_word):
            longest_word = value 
    return longest_word

# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "a=hi b=hello" → opts={"a":"hi","b":"hello"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(longest_value(**opts))