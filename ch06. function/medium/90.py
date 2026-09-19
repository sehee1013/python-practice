# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def first_even(nums):
    """
    정수 리스트 nums에서 처음 나오는 짝수를 반환하기
    
    Args:
        정수 리스트: nums
    Returns:
        int | None : 처음 만난 짝수, 없으면 None
    """
    for num in nums:
        if num % 2 == 0:
            return num
    return None


# 함수 호출 후 결과 출력
print(first_even(nums))