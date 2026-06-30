# chance = 3 로 시작, while chance > 0: 입력 → 비교 → 맞으면 break, 틀리면 chance -= 1
password = "python"
chance = 3

# chance가 0 이상인 동안 비밀번호 맞추기 반복
while chance > 0:
    answer = input()

# 입력한 비밀번호랑 password 맞으면 break , 축하 메세지
    if answer == password:
        print("로그인 성공!")
        break
# 입력한 비밀번호랑 password 안 맞으면 chance -= 1
# 오답 메세지, 남은 기회 출력
    else:
        chance -= 1
        if chance == 0: # 만약 chance == 0 이면 계정 잠김
            print("계정이 잠겼습니다")
        else:
            print("틀렸습니다. 남은 기회:", str(chance) + "번")
