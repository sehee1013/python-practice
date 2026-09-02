# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def list_sum(nums):
    """리스트 원소들의 합 반환하기"""
    return sum(nums)

# 함수 호출 후 출력
print(list_sum(nums))