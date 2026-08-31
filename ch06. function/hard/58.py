# 정수 리스트 nums 를 읽습니다. 예: "1 2" → nums=[1, 2]
nums = [int(x) for x in input().split()]

# reassign(lst) 함수 정의하기
def reassign(lst):
    """lst = [0, 0, 0]으로 재할당"""
    lst = [0, 0, 0]

# mutate(lst) 함수 정의하기
def mutate(lst):
    """lst.append(0) 실행"""
    lst.append(0)

# reassign(nums) 호출
reassign(nums)

# nums 출력
print(nums)

# mutate(nums) 호출
mutate(nums)

# nums 출력
print(nums)