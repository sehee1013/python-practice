# 함수 정의하기
def register(name, **options):
    """
    f"{name}: 키=값,키=값"으로 반환하기

    Args:
        name (str): 이름
        **options: 임의의 추가 옵션
    Returns:
        str: f"{name}: 키=값,키=값" 형식의 문자열
    """
    sorted_options = ','.join(f"{key}={value}" for key, value in sorted(options.items()))
    return f"{name}: {sorted_options}" if sorted_options else f"{name}:"

# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "name=철수 age=20" → opts={"name":"철수","age":"20"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# ↓ 호출부 (수정하지 마세요) — name 은 name 매개변수로, 나머지는 **options 로 모임
print(register(**opts))