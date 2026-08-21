# 전역 name = 첫 단어, age = 둘째 단어. 예: "철수 20" → name="철수", age="20"
parts = input().split()
name = parts[0]
age = parts[1]

# 함수 정의하기
def describe():
    """전역변수 name과 age 읽고 'name(age)' 형식으로 문자열 반환"""
    return f'{name}({age})'

# 함수 호출하여 실행 결과 출력
print(describe())