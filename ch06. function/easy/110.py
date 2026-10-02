# 함수 정의하기
def max_all(*values):
    """
    임의 개수의 정수 중 가장 큰 값을 반환하기

    Args:
        *values (tuple): 정수들
    Returns:
        int: nums 중 가장 큰 값
    """
    max_value = values[0]
    for value in values[1:]:
        if value > max_value:
            max_value = value
    return max_value

# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# ↓ 호출부 (수정하지 마세요)
print(max_all(*nums))