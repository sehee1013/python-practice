age = int(input())
ticket = input().strip()

# 18세 이상이면 계속 진행, 미만이면 18세 미만 입장 불가 메세지 출력
if age >= 18:
# 티켓 있으면 입장 가능 메세지 , 없으면 티켓 구매 메세지 출력
    if ticket == "Y":
        print("입장 가능합니다.")
    else:
        print("티켓을 구매해주세요.")
else:
    print("18세 미만은 입장할 수 없습니다.")