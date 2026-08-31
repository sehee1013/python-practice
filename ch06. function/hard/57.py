# 정수 리스트 nums 를 읽습니다. 예: "5 1 2" → nums=[5, 1, 2]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def double_first(lst):
    """매개변수 lst를 받아 첫 원소를 2배로 만들기"""
    lst[0] = lst[0] * 2

# 함수 호출
double_first(nums)
# nums 출력
print(nums)