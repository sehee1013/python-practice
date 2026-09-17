# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 커트라인(60), 2개면 둘째 값이 커트라인입니다. (정수)
parts = list(map(int, input().split()))

# 함수 정의하기
def check_pass(score, pass_line=60):
    """
    score와 pass_line을 입력받아 합격 여부를 반환하기

    Args:
        score (int): 점수
        pass_line (int): 합격 커트라인 (기본값: 60)
    Returns:
        str: "합격" 또는 "불합격"
    """
    if score >= pass_line:
        return "합격"
    return "불합격"

# 함수 호출 후 출력
print(check_pass(*parts))