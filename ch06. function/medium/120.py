# 함수 정의하기
def report(label, *scores):
    """
    "{label}: {합계}" 형식 문자열을 반환하기

    Args:
        label (str): 라벨
        *scores (int): 점수 튜플
    Returns:
        str: "{label}: {점수들의 합계}"
    """
    return f"{label}: {sum(scores)}"

# 첫 토큰=라벨(label), 나머지=점수들. 예: "수학 90 80 70" → label="수학", scores=[90, 80, 70]
parts = input().split()
label = parts[0]
scores = [int(x) for x in parts[1:]]

# ↓ 호출부 (수정하지 마세요) — label 은 위치 인자, 나머지는 * 로 풀어 전달
print(report(label, *scores))