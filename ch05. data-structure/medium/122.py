email = input()

# @가 있는 경우 @을 기준으로 구분하여 두 번째 원소 출력
if "@" in email:
    _, domain = email.split("@")
    print(domain)
    
# 없는 경우 경고 메시지 출력
else:
    print("유효하지 않은 이메일")