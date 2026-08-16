# 위치 토큰=상품 가격들. "coupon=값" 은 키워드 전용 쿠폰. 예: "100 200 coupon=50" → items=[100,200], coupon=50
raw = input().split()
pos = [t for t in raw if "=" not in t]
items = [int(x) for x in pos]
coupon = 0
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "coupon":
            coupon = int(v)

# 함수 정의하기
def cart(*items, coupon=0):
    """ 상품 합계에서 쿠폰 적용하여 출력하기 """
    # 쿠폰 있는 경우 합 구하고 쿠폰 적용하여 출력
    return sum(items) - coupon

# ↓ 호출부 (수정하지 마세요) — coupon 은 키워드 전용이라 이름으로 전달
print(cart(*items, coupon=coupon))