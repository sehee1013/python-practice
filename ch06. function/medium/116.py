# 함수 정의하기
def range_span(*nums):
    """
    최댓값과 최솟값의 차이 반환하기

    Args:
        nums (tuple): 정수 튜플
    Returns:
        int : 최댓값 - 최솟값
    """
    return max(nums) - min(nums)

# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# ↓ 호출부 (수정하지 마세요)
print(range_span(*nums))