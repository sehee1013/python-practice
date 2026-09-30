# 함수 정의하기
def make_profile(name, age):
    """
    {name}({age}) 를 반환하기

    Args:
        name (str): 이름
        age (str): 나이
    Returns:
        str: "{name}({age})" 형식의문자열
    """
    return f"{name}({age})"


# key=value 토큰을 dict 로 파싱합니다. 예: "name=철수 age=20" → opts={"name":"철수","age":"20"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(make_profile(**opts))