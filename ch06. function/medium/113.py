# 함수 정의하기
def product_all(*nums):
    """
    정수를 모두 곱한 값을 반환하기

    Args:
        nums (tuple): 정수 튜플
    Returns:
        int: 정수를 모두 곱한 값
    """
    total = 1
    for num in nums:
        total *= num
    return total

# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# ↓ 호출부 (수정하지 마세요)
print(product_all(*nums))