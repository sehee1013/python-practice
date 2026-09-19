# 함수 정의하기
def build_tag(name, level=1):
    """
    레벨 수만큼 #를 앞에 붙인 문자열을 반환하기

    Args:
        name (str): 제목
        level (int): 레벨 (기본값: 1)
    Returns:
        str: "#" * level + name
    """
    return "#" * level + name

# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 레벨(1), 2개면 둘째 값(정수)이 레벨입니다.
parts = input().split()

# level 입력 있는 경우 정수형으로 변환하기
if len(parts) == 2:
    name, level = parts[0], int(parts[1])
else:
    name = parts[0]
    level = 1

# 함수 호출 후 출력
print(build_tag(name, level))