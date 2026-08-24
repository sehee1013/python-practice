# 첫 값=초기 잔액, 나머지=증감액. 예: "1000 100 -50 200" → balance=1000, changes=[100,-50,200]
parts = input().split()
balance = int(parts[0])
changes = [int(x) for x in parts[1:]]

# 함수 정의
def apply(amount):
    """전역변수 balance(잔액)에 증감액 더하여 반환하기"""
    # balance를 global 선언하기
    global balance
    # balance에 증감액 더하기
    balance += amount

# 리스트 순회하며 balance에 증감액 더하기
for change in changes:
    apply(change)

# balance 출력
print(balance)