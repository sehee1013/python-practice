# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "130" 이면 sec == 130
sec = int(input())

# 함수 정의하기
def sec_to_str(sec):
    """정수 sec 를 {분}분 {초}초 형식의 문자열을 반환하기"""
    minutes = sec // 60
    seconds = sec % 60
    return f"{minutes}분 {seconds}초"

# 함수 호출 후 출력하기
print(sec_to_str(sec))