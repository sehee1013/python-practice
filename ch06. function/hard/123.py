# 함수 정의하기
def top_k_sum(k, *nums):
    """
    가장 큰 k 개의 합을 반환하기

    Args:
        k (int): 개수
        *nums(tuple): 정수 튜플
    Returns:
        int: 가장 큰 k 개의 합
    """
    sorted_nums = sorted(nums, reverse=True)
    return sum(sorted_nums[:k])

# 첫 토큰=개수(k), 나머지=정수들. 예: "2 1 2 3 4" → k=2, nums=[1, 2, 3, 4]
parts = input().split()
k = int(parts[0])
nums = [int(x) for x in parts[1:]]

# ↓ 호출부 (수정하지 마세요) — k 는 위치 인자, 나머지는 * 로 풀어 전달
print(top_k_sum(k, *nums))