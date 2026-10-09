# 함수 정의하기
def ranking(category, *names):
    """
    {카테고리}: 항목1 > 항목2 > ... 형식으로 반환하기

    Args:
        category (str): 카테고리 이름
        *names: 임의 개수의 항목
    Returns:
        str: {카테고리}: 항목1 > 항목2 > ... 형식의 문자열
    """
    return f"{category}: {' > '.join(names)}"

# 첫 토큰=카테고리, 나머지=항목들. 예: "선호도 사과 바나나" → category="선호도", names=["사과","바나나"]
raw = input().split()
category = raw[0]
names = raw[1:]

# ↓ 호출부 (수정하지 마세요)
print(ranking(category, *names))