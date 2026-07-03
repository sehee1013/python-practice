# 무게 판정 → 옵션 입력 → 최종 배송 방식 출력.
weight = float(input())
option = input()

# 배송 방식: 무게 2kg 이상 미만 확인 -> 옵션 선택 순으로 결정
# 2kg 이상은 빠른 배송 여부 선택
if weight >= 2:
    if option == "Y":
        delivery_type, price = "택배(빠른 배송)", 5000
    else:
        delivery_type, price = "택배(일반 배송)", 3000
# 2kg 미만은 등기, 일반 중 선택
else:
    if option == "Y":
        delivery_type, price = "우편(등기)", 2000
    else:
        delivery_type, price = "우편(일반)", 1000

# 배송 방법, 요금 출력
print(f"{delivery_type} - {price}원")