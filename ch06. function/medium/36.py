# 전역 name = 첫 단어, guest = 둘째 단어. 예: "주인 손님" → name="주인", guest="손님"
parts = input().split()
name = parts[0]
guest = parts[1]

# 함수 정의하기
def greet(name):
    """매개변수 name을 받아 인사 메시지 반환"""
    return f"안녕, {name}"

# 함수 호출하여 실행 결과 출력
print(greet(guest))
# 전역변수 name 출력
print(name)