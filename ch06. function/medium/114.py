# 함수 정의하기
def count_even(*nums):
    """
    임의 개수의 정수 중 짝수의 개수 반환하기

    Args:
        nums (tuple): 정수 튜플
    Returns:
        int: 짝수의 개수
    """
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# ↓ 호출부 (수정하지 마세요)
print(count_even(*nums))