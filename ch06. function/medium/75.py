# input() 으로 문자열 한 줄을 읽습니다. 예: 입력이 "hello" 이면 s == "hello"
s = input()

# 함수 정의하기
def count_vowels(s):
    """영어 소문자로 된 문자열 s를 입력받아 모음 개수 반환하기"""
    count = 0
    for char in s:
        if char in "aeiou":
            count += 1
    return count

# 함수 호출 후 출력
print(count_vowels(s))