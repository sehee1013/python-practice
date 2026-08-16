# 위치 토큰=이름, "key=value" 토큰들=설정. 예: "서버 host=localhost port=8080" → name="서버", settings={...}
raw = input().split()
name = ""
settings = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        settings[k] = v
    else:
        name = t

# 함수 정의하기
def config(name, **settings):
    # "{name} has {개수} settings" 형식으로 출력
    return f"{name} has {len(settings)} settings"

# ↓ 호출부 (수정하지 마세요)
print(config(name, **settings))