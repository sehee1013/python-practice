# 전역 status 시작값 "대기". 설정할 상태들을 순서대로 읽습니다. 예: "진행 완료" → commands=["진행","완료"]
status = "대기"
commands = input().split()

# 함수 정의하기
def set_status(new):
    """전역 status를 new 값으로 갱신"""
    # 전역변수 status global 선언
    global status
    # status에 new 대입
    status = new

# 함수 호출 후 실행
for cmd in commands:
    set_status(cmd)

# 결과 출력
print(status)