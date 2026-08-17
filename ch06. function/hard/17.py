raw = input().split()
pos = [t for t in raw if "=" not in t]
product = pos[0]
price = int(pos[1])
options = pos[2:]
discount = 0
info = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "discount":
            discount = int(v)
        else:
            info[k] = v

# 함수 정의하기
def order2(product, price, *options, discount=0, **info):
    """상품명, 가격(할인 적용가), 옵션 개수, 옵션 상세내용 출력"""
    # 옵션 키, 키값 리스트 추가
    option_info = [f"{key}={value}" for key, value in sorted(info.items())]
    # {product} {price-discount}원 옵션{옵션개수}개 [기타정보를 키 사전순 'k=v' 로 ','연결]" 형식으로 반환
    return f"{product} {price - discount}원 옵션{len(options)}개 [{','.join(option_info)}]"

# ↓ 호출부 (수정하지 마세요)
print(order2(product, price, *options, discount=discount, **info))