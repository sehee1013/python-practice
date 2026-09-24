# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "3 -1 4" → nums=[3, -1, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def first_negative(nums):
    """
    정수 리스트에서 첫 음수를 찾으면 조기 종료
    
    args: 정수 리스트
    returns: int 처음 찾은 음수, 없는 경우 str "없음"
    """
    for num in nums:
        if num < 0:
            return num
    return "없음"

# 함수 호출 후 결과 출력
print(first_negative(nums))