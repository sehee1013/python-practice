# 함수 정의하기
def announce():
    """전역 message를 읽어 공지 형식의 문자열 반환"""
    return f"[공지] {message}"

# 전역변수 message 를 입력에서 읽습니다. 예: "회의 3시" → message="회의 3시"
message = input()

# 함수 호출하여 결과 출력
print(announce())