raw = input().split()
pos = [t for t in raw if "=" not in t]
base = int(pos[0])
items = [int(x) for x in pos[1:]]
tax = 0
fees = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "tax":
            tax = int(v)
        else:
            fees[k] = int(v)

# 함수 정의하기
def invoice(base, *items, tax=0, **fees):
    """기본가(필수), 임의 개수의 품목 금액, 세율(키워드 전용),
    그 외 추가 비용 항목(가변 키워드)을 받아 총액을 반환"""
    return base + base*tax // 100 + sum(items) + sum(fees.values())

# ↓ 호출부 (수정하지 마세요)
print(invoice(base, *items, tax=tax, **fees))