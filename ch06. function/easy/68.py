# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "95" 이면 score == 95
score = int(input())

# 함수 정의하기
def grade(score):
    """score로 등급 판별하기"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

# 함수 호출 후 출력
print(grade(score))