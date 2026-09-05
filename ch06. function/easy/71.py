# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 -2 3" → nums=[1, -2, 3]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def count_positive(nums):
    """리스트에서 양수의 개수 반환하기"""
    count = 0
    for n in nums:
        if n > 0:
            count += 1
    return count

# 함수 호출 후 출력
print(count_positive(nums))