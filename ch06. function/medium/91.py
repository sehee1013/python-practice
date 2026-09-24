# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "-5" 이면 n == -5
n = int(input())

# 함수 정의하기
def abs_sign(n):
    """
    정수 n을 입력받아, 절대값과 부호 문자열을 함께 반환하기
    
    Args:
        n (int): 입력 정수
    Returns:
        tuple[int, str]: 절대값, 부호 문자열(양수면 "양수", 음수면 "음수", 0이면 "0")    
    """
    abs_n = abs(n)
    if n > 0:
        return abs_n, "양수"
    elif n < 0:
        return abs_n, "음수"
    return 0, "0"
    

# 함수 호출 후 언패킹
abs_n, sign_n = abs_sign(n)

# 결과 출력
print(abs_n, sign_n)