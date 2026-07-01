new_price = int(input())
year = int(input())
km = float(input())
accident = input()

accident_discount = 0

# 연식에 따른 감가율 판별
if year <= 3:
    year_discount = year * 10
elif year <= 7:
    year_discount = 3 * 10 + (year - 3) * 7
else:
    year_discount = 3 * 10 + 4 * 7 + (year - 7) * 5

# 주행거리에 따른 감가율 판별
if km <= 5:
    km_discount = 0
elif km <= 10:
    km_discount = 5
else:
    km_discount = 10

# 사고 유무에 따른 감가율 판별
if accident.strip().upper() == "Y":
    accident_discount = 15
elif accident.strip().upper() == "N":
    accident_discount = 0

# 총 감가율 계산 
total_discount = km_discount + year_discount + accident_discount
# 최종 가격 계산
total_price = int(new_price * (1 - total_discount / 100))

# 최소 가격 구한 후 최종 가격보다 크면 최소 가격이 최종가격
minimum_price = int(new_price * 0.1)

if total_price < minimum_price:
    total_price = minimum_price

# 결과 출력
print("--- 감가 내역 ---")
print(f"연식 감가 ({year}년): {year_discount}%")
print(f"주행거리 감가: {km_discount}%")
print(f"사고 감가: {accident_discount}%")
print(f"총 감가율: {total_discount}%")
print(f"예상 중고차 가격: {total_price}만원")