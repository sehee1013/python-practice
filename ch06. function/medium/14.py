raw = input().split()
pos = [t for t in raw if "=" not in t]
event = pos[0]
details = pos[1:]
level = "INFO"
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "level":
            level = v

# 함수 정의하기
def log_event(event, *details, level="INFO"):
    """{level}: {event} ({details 개수}) 형식으로 반환"""
    return f"{level}: {event} ({len(details)})"

# ↓ 호출부 (수정하지 마세요) — level 은 키워드 전용이라 이름으로 전달
print(log_event(event, *details, level=level))