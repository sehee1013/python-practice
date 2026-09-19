# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "85" 이면 score == 85
score = int(input())

# 함수 정의하기
def evaluate(score):
    """정수 점수 score를 입력받아 검증하기"""
    # 0 미만 100 초과시 "유효하지 않음" 반환
    if score < 0 or score > 100:
        return "유효하지 않음"
    # 60 이상은 "합격", 미만은 "불합격" 반환
    if score >= 60:
        return "합격"
    else:
        return "불합격"

# 함수 호출 후 결과 출력
print(evaluate(score))