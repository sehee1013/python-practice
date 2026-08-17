raw = input().split()
pos = [t for t in raw if "=" not in t]
first = pos[0]
rest = pos[1:]
sep = "-"
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "sep":
            sep = v

# 함수 정의하기
def make_list(first, *rest, sep="-"):
    """구분자로 입력받은 문자 잇기 """
    # 리스트 합치기
    parts = [first] + list(rest)
    return sep.join(parts)

# ↓ 호출부 (수정하지 마세요) — sep 은 키워드 전용이라 이름으로 전달
print(make_list(first, *rest, sep=sep))