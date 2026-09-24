# 함수 정의하기
def average_args(*nums):
    """
    정수들의 평균을 반환하기

    Args:
        nums (tuple): 정수 튜플
    Returns:
        int: 평균 (나머지 버림)
    """
    return sum(nums) // len(nums)

# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# ↓ 호출부 (수정하지 마세요)
print(average_args(*nums))