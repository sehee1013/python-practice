# 흐름: 입력 읽기 -> 함수 호출 -> 결과 출력
parts = input().split()
host = parts[0]
port = parts[1]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def connect(host, *, port):
    return host + ":" + port

# 함수 호출하여 결과 출력
print(connect(host, port=port))