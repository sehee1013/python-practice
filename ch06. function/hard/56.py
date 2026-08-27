# 문자열 text 를 입력에서 읽습니다. 예: "hi" → text="hi"
text = input()

# 함수 정의하기
def shout(s):
    """매개변수 s를 받아 s = s + '!' 후 반환"""
    s = s + "!"
    return s

# 함수 호출 후 출력
print(shout(text))
# text 출력
print(text)