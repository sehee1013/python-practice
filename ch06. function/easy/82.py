# input() 으로 이름 한 줄을 읽습니다. 예: 입력이 "철수" 이면 name == "철수"
name = input()

# 함수 정의하기
def welcome(name):
    """'{이름}님 환영합니다' 를 함수 안에서 출력하기"""
    print(f"{name}님 환영합니다")

# 함수 호출 후 출력
print(welcome(name))