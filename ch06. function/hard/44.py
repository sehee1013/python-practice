# 전역 language = 첫 단어, chosen = 둘째 단어. 예: "한국어 영어" → language="한국어", chosen="영어"
parts = input().split()
language = parts[0]
chosen = parts[1]

# 함수 정의하기
def setting():
    """지역변수 language = chosen 으로 두고 "현재: " + language 형식으로 문자열 반환"""
    language = chosen
    return f"현재: {language}"

# 함수 정의하기
def reading():
    """기본: + language 형식으로 문자열 반환"""
    return f"기본: {language}"

# setting() 호출하여 실행 결과 출력
print(setting())
# reading() 호출하여 실행 결과 출력
print(reading())
# 전역변수 language 출력
print(language)