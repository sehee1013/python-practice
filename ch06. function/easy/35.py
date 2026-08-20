# 첫 값=가격(price0), 둘째 값=전역 세율 rate. 예: "1000 10" → price0=1000, rate=10
parts = input().split()
price0 = int(parts[0])
rate = int(parts[1])

# 함수 정의하기
def apply(price):
    """가격 매개변수 price로 세율을 이용해 부가세 포함 가격 반환"""
    return price + (price * rate) // 100

# 함수 호출하여 실행 결과 출력
print(apply(price0))