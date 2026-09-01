# 이름을 한 줄로 읽습니다. 예: "철수" → name="철수"
name = input()

# 함수 정의하기
def greet(name):
    """이름으로 인사말을 만든다."""
    return f"안녕하세요, {name}님!"

# greet.__doc__ 출력
print(greet.__doc__)
# greet(name) 호출 후 출력
print(greet(name))