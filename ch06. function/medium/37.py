# 첫 값=요청 수량 n, 둘째 값=전역 재고 stock. 예: "5 10" → n=5, stock=10
parts = input().split()
n = int(parts[0])
stock = int(parts[1])

# 함수 정의하기
def in_stock(n):
    """재고와 요청 수량 비교하여 재고가 요청 수량보다 많거나 같으면 "가능", 그렇지 않으면 "불가" 반환"""
    # 재고가 더 많은 경우
    if stock >= n:
        return "가능"
    return "불가"

# 함수 호출하여 실행 결과 출력
print(in_stock(n))