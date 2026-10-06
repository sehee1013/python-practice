# 함수 정의하기
def total_with_tax(price, tax):
    """
    price와 tax를 받아 세금 포함 금액을 반환하기

    Args:
        price (int): 가격
        tax (int): 세율
    Returns:
        int: 세금 포함한 금액
    """
    return price + price * tax // 100

# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "price=1000 tax=10" → opts={"price":1000,"tax":10}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(total_with_tax(**opts))