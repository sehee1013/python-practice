# 함수 정의하기
def concat_words(*words):
    """
    '-'로 이어 붙인 문자열 반환하기

    Args:
        *words (str): 입력받은 문자열
    Returns:
        str: '-'를 구분자로 한 문자열
    """
    return '-'.join(words)

# 입력을 단어 리스트로 만듭니다. 예: "a b c" → words=["a", "b", "c"]
words = input().split()

# ↓ 호출부 (수정하지 마세요)
print(concat_words(*words))