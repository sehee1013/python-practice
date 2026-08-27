# 정수 리스트 nums 를 읽습니다. 예: "1 2" → nums=[1, 2]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def append_99(lst):
    """매개변수 lst를 받아 lst.append(99)를 정의"""
    lst.append(99)
    
# 함수 호출
append_99(nums)
# nums 출력
print(nums)