# 전역 amount = 첫 값, rate = 둘째 값. 예: "1000 10" → amount=1000, rate=10
parts = input().split()
amount = int(parts[0])
rate = int(parts[1])

# 함수 정의하기
def tax_of():
    """전역변수 amount와 rate를 읽고 계산하여 세금 반환하기"""
    return amount * rate // 100

# 함수 호출하여 실행 결과 출력하기
print(tax_of())