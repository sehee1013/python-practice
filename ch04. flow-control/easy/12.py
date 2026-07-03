# 설정된 비밀번호와 입력값을 비교하세요.
password = "python123"
user_input = input()

# 입력된 비밀번호랑 설정된 비밀번호랑 같으면 "로그인 성공" 출력
if user_input == password:
    print("로그인 성공")
# 틀리면 "비밀번호 오류", "다시 시도하세요" 출력
else:
    print("비밀번호 오류")
    print("다시 시도하세요")