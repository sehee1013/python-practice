# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def stats(nums):
    """
    정수 리스트의 최솟값,최댓값, 합을 함께 반환하기
    
    args: 정수 리스트 nums
    returns: int 최솟값, 최댓값, 합
    """
    min_nums = min(nums)
    max_nums = max(nums)
    total_sum = sum(nums)
    return min_nums, max_nums, total_sum

# 함수 호출 후 결과 출력
print(*stats(nums))