# 함수 정의하기
def rectangle_kw(width, height):
    """
    가로 길이와 세로 길이를 키워드 인자로 받아 넓이 반환하기

    Args:
        width (int): 가로 길이
        height (int): 세로 길이
    Returns:
        int: 넓이
    """
    return width * height
    
# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "width=4 height=5" → opts={"width":4,"height":5}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(rectangle_kw(**opts))