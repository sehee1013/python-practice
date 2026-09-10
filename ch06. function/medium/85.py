# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def sum_avg(nums):
    """합과 평균(정수 나눗셈, 버림)을 함께 반환하기"""
    nums_sum = sum(nums)
    nums_avg = nums_sum // len(nums)
    return nums_sum, nums_avg

# 함수 호출 후 언패킹
nums_sum, nums_avg = sum_avg(nums)

# 결과 출력
print(nums_sum, nums_avg)