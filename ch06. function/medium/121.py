# 함수 정의하기
def count_above(threshold, *nums):
    """
    threshold 보다 큰 값의 개수를 반환하기

    Args:
        threshold (int): 기준
        *nums (tuple): 정수 튜플
    Returns:
        int: nums 중 threshold보다 큰 값의 개수를 반환하기
    """
    count = 0
    for num in nums:
        if num > threshold:
            count += 1
    return count

# 첫 토큰=기준값(threshold), 나머지=검사할 정수들. 예: "5 3 6 1 8" → threshold=5, nums=[3, 6, 1, 8]
parts = input().split()
threshold = int(parts[0])
nums = [int(x) for x in parts[1:]]

# ↓ 호출부 (수정하지 마세요) — threshold 는 위치 인자, 나머지는 * 로 풀어 전달
print(count_above(threshold, *nums))