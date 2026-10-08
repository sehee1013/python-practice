# 함수 정의하기
def invoice(base, **fees):
    """
    기본가에 모든 추가 비용을 더한 합계를 반환하기

    Args:
        base (int): 기본가
        **fees: 임의의 추가 비용 항목
    Returns:
        int: 기본가에 모든 추가 비용을 더한 합계
    """
    return base + sum(fees.values())

# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "base=1000 ship=500" → opts={"base":1000,"ship":500}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# ↓ 호출부 (수정하지 마세요) — base 는 base 매개변수로, 나머지는 **fees 로 모임
print(invoice(**opts))