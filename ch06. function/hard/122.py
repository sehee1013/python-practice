# 함수 정의하기
def trimmed_sum(*nums):
    """
    최댓값 하나와 최솟값 하나를 뺀 나머지의 합을 반환하기

    Args:
        *nums (tuple): 정수 튜플
    Returns:
        int: 최댓값 하나와 최솟값 하나를 뺀 나머지의 합
    """
    return sum(nums) - max(nums) - min(nums)

# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4 5" → nums=[1, 2, 3, 4, 5]
nums = [int(x) for x in input().split()]

# ↓ 호출부 (수정하지 마세요)
print(trimmed_sum(*nums))