# 흐름: 입력 읽기 -> 함수 호출 -> 함수 실행 결과 출력
raw = input().split()
pos = [t for t in raw if "=" not in t]
endpoint = pos[0]
args = pos[1:]
method = "GET"
headers = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "method":
            method = v
        else:
            headers[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def api(endpoint, *args, method="GET", **other):
    return endpoint + " " + method + " a" + str(len(args)) + " h" + str(len(other))

# 함수 호출하여 실행 결과 출력하기
print(api(endpoint, *args, method=method, **headers))