# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 age, city 가 기본값으로 채워집니다. (age 는 정수)
parts = input().split()

# 이름만 있는 경우
if len(parts) == 1:
    new_parts = parts
# 이름과 나이만 있는 경우
elif len(parts) == 2:
    new_parts = [parts[0], int(parts[1])]
# 이름, 나이, 도시가 있는 경우
elif len(parts) == 3:
    new_parts = [parts[0], int(parts[1]), parts[2]]
    
# 함수 정의하기
def introduce(name, age=20, city="서울"):
    """
    이름과 나이·도시를 입력받아 {이름}/{나이}/{도시} 를 반환하기
    
    Args: 
        name (str): 이름
        age (int): 나이 (기본값: 20)
        city (str): 도시 (기본값: "서울")
    Returns:
        str: {name}/{age}/{city} 형식의 문자열
    """
    return f"{name}/{age}/{city}"

# 함수 호출 후 출력
print(introduce(*new_parts))