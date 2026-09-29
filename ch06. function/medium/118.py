# 함수 정의하기
def first_and_last_sum(*nums):
    """
    첫 번째 인자와 마지막 인자의 합을 반환하기

    Args:
        *nums (tuple): 정수 튜플 (가변인자)
    Returns:
        int: 첫 번째 인자와 마지막 인자의 합
    """
    return nums[0] + nums[-1]

# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# ↓ 호출부 (수정하지 마세요)
print(first_and_last_sum(*nums))