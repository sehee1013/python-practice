# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def total(*values):
    """
    정수 리스트를 받아 합을 반환하기
    
    Args:
        values (tuple): 더해야하는 값
    Returns:
        int: values 정수들의 합
    """
    return sum(values)

# ↓ 호출부 (수정하지 마세요) — 리스트를 * 로 풀어 total 에 전달
print(total(*nums))