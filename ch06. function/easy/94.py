# 한 줄을 공백으로 나눕니다. 예: "철수" → ["철수"](기본값 사용) / "철수 반가워" → ["철수","반가워"](override)
parts = input().split()

# 함수 정의하기
def greet(name, greeting="안녕하세요"):
    """
    이름과 인사말을 반환하기

    Args:
        name (str): 입력받은 이름
        greeting (str): 인사말, 기본값("안녕하세요")
    Returns:
        str: "{greeting}, {name}님!" 형식의 문자열
    """
    return f"{greeting}, {name}님!"

# 함수 호출 후 출력
print(greet(*parts))