# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "10 2" → a=10, b=2
dividend, divisor = [int(x) for x in input().split()]

# 함수 정의하기
def safe_divide(dividend, divisor):
    """두 정수 dividend와 divisor를 입력 받아 dividend // divisor 결과 반환하기"""
    # divisor 가 0 이면 즉시 "오류" 를 반환
    if divisor == 0:
        return "오류"
    return dividend // divisor

# 함수 호출 후 출력
print(safe_divide(dividend, divisor))