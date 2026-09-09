# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def min_max(nums):
    """정수 리스트의 최솟값과 최댓값 반환하기"""
    return min(nums), max(nums)

# 함수 호출하고 결과 언패킹하기
min_num, max_num = min_max(nums)
# 결과 출력하기
print(min_num, max_num)