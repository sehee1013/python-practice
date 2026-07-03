user_id = input().strip()
password = input().strip()

# id 딕셔너리 생성
user_information = {
    "admin" : "1234"
}
# id 맞으면 계속 진행, 틀리면  id 존재 안함 메시지 출력
if user_id in user_information:
    # 비밀번호 맞으면 로그인 성공, 틀리면 비밀번호 틀림 메시지 출력
    if password == user_information[user_id]:
        print("로그인 성공!")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("ID가 존재하지 않습니다.")