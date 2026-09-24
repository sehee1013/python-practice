# 함수 정의하기
def min_all(*nums):
    """
    정수 리스트 중 가장 작은 값을 반환하기
    
    Args:
        nums (tuple): 정수 튜플
    Returns:
        int: 가장 작은 수
    """
    min_value = nums[0]
    for num in nums[1:]:
        if num < min_value:
            min_value = num
    return min_value

# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# ↓ 호출부 (수정하지 마세요)
print(min_all(*nums))