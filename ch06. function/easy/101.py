# 한 줄을 공백으로 나눕니다. 토큰이 2개면 기본 구분자("-"), 3개면 셋째 값이 구분자입니다.
parts = input().split()

# 함수 정의하기
def join_two(a, b, sep="-"):
    """
    두 단어 a, b와 구분자 sep을 입력받아 a + sep + b를 반환하기

    Args:
        a (str): 첫 번째 단어
        b (str): 두 번째 단어
        sep (str): 구분자 (기본값: "-")
    Returns:
        str: a + sep + b
    """
    return a + sep + b

# 함수 호출 후 출력
print(join_two(*parts))