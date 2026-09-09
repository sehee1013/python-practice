# input() 으로 문자열 한 줄을 읽습니다. 예: 입력이 "racecar" 이면 s == "racecar"
s = input()

# 함수 정의하기
def is_palindrome(s):
    """문자열 s가 회문이면 True, 아니면 False 반환하기"""
    return s == s[::-1]

# 함수 호출 후 출력
print(is_palindrome(s))