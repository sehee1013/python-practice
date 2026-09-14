# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 2회, 2개면 둘째 값(정수)이 반복 횟수입니다.
parts = input().split()
int_parts = [parts[0]] + list(map(int, parts[1:]))

# 함수 정의하기
def repeat_text(text, times=2):
    """
    text와 times를 입력받아 text * times를 반환하기
    
    Args:
        text (str): 출력할 문자열
        times (int): 반복 횟수
    Returns:
        str: 문자열 반복 출력
    """
    return text * times

# 함수 호출 후 출력
print(repeat_text(*int_parts))