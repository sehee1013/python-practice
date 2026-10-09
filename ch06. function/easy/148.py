# 함수 정의하기
def menu(name, *sides):
    """
    대표 메뉴 이름과 임의 개수의 사이드 메뉴를 받아 문자열로 반환하기

    Args:
        name (str): 대표 메뉴 이름
        *sides: 임의 개수의 사이드 메뉴 이름
    Returns:
        str: 대표 메뉴 (사이드 메뉴) 형식의 문자열
    """
    return f"{name} ({','.join(sides)})" if sides else name

# 첫 토큰=대표 메뉴, 나머지=사이드. 예: "비빔밥 김치 단무지" → name="비빔밥", sides=["김치","단무지"]
raw = input().split()
name = raw[0]
sides = raw[1:]

# ↓ 호출부 (수정하지 마세요)
print(menu(name, *sides))