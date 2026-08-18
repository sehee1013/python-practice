raw = input().split()
pos = [t for t in raw if "=" not in t]
name = pos[0]
roles = pos[1:]
status = "active"
meta = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "status":
            status = v
        else:
            meta[k] = v

# 함수 정의하기
def profile(name, *roles, status="active", **meta):
    """입력받은 정보로 프로필 요약하여 반환"""
    return f"{name}[{status}] 역할{len(roles)} 정보{len(meta)}"
    
# ↓ 호출부 (수정하지 마세요)
print(profile(name, *roles, status=status, **meta))