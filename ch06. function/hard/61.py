# key=value 토큰을 dict 로 읽습니다(값은 정수). 예: "a=100 b=200" → prices={"a":100,"b":200}
prices = {}
for t in input().split():
    k, v = t.split("=")
    prices[k] = int(v)

# 함수 정의하기
def discount_all(d):
    """매개변수 d의 모든 값을 10씩 줄이기"""
    for k in d:
        d[k] -= 10

# 함수 호출
discount_all(prices)

# ↓ 출력부 (제공됨) — 호출 후 바뀐 prices 를 키 사전순으로 출력
items = []
for k in sorted(prices):
    items.append(k + "=" + str(prices[k]))
print(",".join(items))