# 바깥 if는 파일명, 안쪽 if는 확장자 기준으로 작성하세요.
filename = input()
extension = input()

# 파일명 있는 경우
if filename:
    # 확장자가 txt인 경우
    if extension == "txt":
        print("텍스트 파일 저장")
    # 확장자 txt 아닌 경우
    else:
        print("지원되지 않는 형식")
# 파일명이 빈 문자열인 경우
else:
    print("파일명을 입력하세요")