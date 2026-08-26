# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "5" 이면 n == 5
n = int(input())

# 함수 정의하기
def sign(n):
    """
    정수 n의 부호에 따라 문자열 반환
    양수 -> "양수"
    음수 -> "음수"
    0 -> "0"
    """
    if n > 0:
        return "양수"
    elif n < 0:
        return "음수"
    return "0"

# 함수 호출 후 결과 출력
print(sign(n))