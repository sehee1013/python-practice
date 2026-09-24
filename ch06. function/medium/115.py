# 함수 정의하기
def sum_positive(*nums):
    """
    임의 개수의 정수를 받아 그 중 양수만 더한 합 반환하기

    Args:
        nums (tuple): 정수 튜플
    Returns:
        int: 양수만 더한 합
    """
    total = 0
    for num in nums:
        if num > 0:
            total += num
    return total

# 입력을 정수 리스트로 만듭니다. 예: "1 -2 3" → nums=[1, -2, 3]
nums = [int(x) for x in input().split()]

# ↓ 호출부 (수정하지 마세요)
print(sum_positive(*nums))