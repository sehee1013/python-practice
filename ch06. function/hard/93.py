# 첫 줄은 한계값 T, 둘째 줄은 공백으로 구분된 정수들입니다.
# 예: 첫 줄 "10", 둘째 줄 "3 4 5 6" → threshold=10, nums=[3, 4, 5, 6]
threshold = int(input())
nums = [int(x) for x in input().split()]

# 함수 정의하기
def first_exceed(nums, threshold):
    """
    누적합이 처음으로 정수 T를 초과하는 위치의 인덱스를 찾는 즉시 반환하기
    
    Args:
        nums (list): 입력받은 정수형 리스트
        threshold (int): 한계값
    Returns:
        idx (int): 처음으로 T를 초과하는 위치의 인덱스, 없으면 -1 반환
    """
    total_sum = 0
    for idx, value in enumerate(nums):
        total_sum += value
        if total_sum > threshold: # 초과하면 즉시 반환하고 종료 
            return idx
    return -1 # 마지막까지 초과하지 못할 경우

# 함수 호출 후 결과 출력
print(first_exceed(nums, threshold))