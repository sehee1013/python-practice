# 함수 정의하기
def count_args(*args):
    """
    받은 인자의 개수 반환하기

    Args:
        *args: 정수 0개 이상
    Returns:
        int: 인자의 개수
    """
    return len(args)

# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# ↓ 호출부 (수정하지 마세요)
print(count_args(*nums))