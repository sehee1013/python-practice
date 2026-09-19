# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "3661" 이면 sec == 3661
sec = int(input())

# 함수 정의하기
def to_hms(sec):
    """정수 sec을 입력받아 시, 분, 초 세 값을 함께 반환하기"""
    hours = sec // 3600
    minutes = (sec % 3600) // 60
    seconds = sec % 60
    return hours, minutes, seconds

# 함수 호출 후 언패킹
hours, minutes, seconds = to_hms(sec)

# 결과 출력
print(hours, minutes, seconds)