# input() 으로 문자열 한 줄을 읽습니다. 예: 입력이 "hello" 이면 s == "hello"
s = input()

# 함수 정의하기
def reverse(s):
    """문자열 s를 뒤집어서 반환하기"""
    return s[::-1]

# 함수 호출 후 출력
print(reverse(s))