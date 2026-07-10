menu = ("Espresso", "Latte", "Cappuccino", "Americano")
order = input()

# 주문이 메뉴 tuple에 있으면 주문 가능. 그 외는 주문 불가
if order in menu:
    print("주문 가능")
else:
    print("주문 불가")