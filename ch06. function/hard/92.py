# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def stats4(nums):
    """
    정수 리스트의 최솟값, 최댓값, 합, 평균을 반환하기
    
    Args:
        nums (int list): 입력 받은 정수형 리스트
    Returns:
        tuple(int): 최솟값, 최댓값, 합, 평균(나머지 버림)
    """
    min_val = min(nums) 
    max_val = max(nums)
    total_sum = sum(nums)
    avg = total_sum // len(nums)
    return min_val, max_val, total_sum, avg

# 함수 호출 후 언패킹
min_val, max_val, total_sum, avg = stats4(nums)

# 결과 출력
print(min_val, max_val, total_sum, avg)