weight = int(input())
dist = int(input())
price = 3000

# 무게 추가요금 판별
if weight <= 2:
    pass
elif weight <= 10:
    price += 1000
else:
    price += 3000

# 거리 추가요금 판별
if dist <= 50:
    pass
elif dist <= 100:
    price += 1500
else:
    price += 3000

# 결과 출력
print(f"무게: {weight}kg | 거리: {dist}km")
print(f"택배 요금: {price}원")