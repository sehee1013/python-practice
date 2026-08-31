# 정수 리스트 nums 를 읽습니다. 예: "1 2" → nums=[1, 2]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def add_to_copy(lst):
    """매개변수 lst의 복사본을 만들어 거기에 99를 추가하기"""
    copied = lst[:]
    copied.append(99)
    return copied

# 함수 호출 후 반환값 출력
print(add_to_copy(nums))

# nums 출력
print(nums)