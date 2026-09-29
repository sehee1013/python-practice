# 함수 정의하기
def sum_scaled(factor, *nums):
    """
    정수들의 합에 factor를 곱한 값을 반환하기

    Args:
        factor (int): 배수
        *nums (tuple): 정수 튜플
    Returns:
        int: nums들의 합 * factor
    """
    return sum(nums) * factor
    
# 첫 토큰=배수(factor), 나머지=더할 정수들. 예: "2 1 2 3" → factor=2, nums=[1, 2, 3]
parts = input().split()
factor = int(parts[0])
nums = [int(x) for x in parts[1:]]

# ↓ 호출부 (수정하지 마세요) — factor 는 위치 인자, 나머지는 * 로 풀어 전달
print(sum_scaled(factor, *nums))