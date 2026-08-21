# 전역 nums 를 정수 리스트로 읽습니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def total():
    """전역 nums를 읽고 원소들의 합 반환하기"""
    return sum(nums)

# 함수 호출하고 실행하여 결과 출력
print(total())