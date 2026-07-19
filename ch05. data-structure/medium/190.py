# 가격표를 dict 로 조회해 각 항목 출력 + 누적합산.
menu = {"커피": 4000, "라떼": 5000, "차": 3000, "케이크": 6000}
n = int(input())
total_charge = 0

# n번 메뉴 입력 받기
for _ in range(n):
    order = input()
    
    # 주문내역 메뉴: 가격 형식으로 출력
    print(f"{order}: {menu[order]}원")
    total_charge += menu[order]

# 총액 출력
print(f"합계: {total_charge}원")