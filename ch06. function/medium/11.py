# 위치 토큰: 첫째=제목, 나머지=정수. "unit=값" 은 키워드 전용 단위.
# 예: "거리 10 20 unit=km" → title="거리", values=[10,20], unit="km"
raw = input().split()
pos = [t for t in raw if "=" not in t]
title = pos[0]
values = [int(x) for x in pos[1:]]
unit = "개"

for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "unit":
            unit = v

# report 함수 정의하기
def report(title, *values, unit="개"):
    """{title}: {values의 합}{unit} 형식으로 반환하기"""
    return f"{title}: {sum(values)}{unit}"

print(report(title, *values, unit=unit))