# input().split() 으로 두 칸을 나눕니다. 예: "김 철수" → last="김", first="철수"
last, first = input().split()

# 함수 정의하기
def name_order(last, first):
    """성 이름을 한 줄로 입력받아 이름과 성을 순서로 함께 반환하기 """
    return first, last

# 함수 호출 후 언패킹
first_name, last_name = name_order(last, first)

# 결과 출력
print(first_name, last_name)