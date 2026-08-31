# 첫 값=정수 n, 나머지=리스트 items. 예: "5 1 2" → n=5, items=[1, 2]
parts = input().split()
n = int(parts[0])
items = [int(x) for x in parts[1:]]

# 함수 정의하기
def change_both(num, lst):
    """정수 n과 정수 리스트 items를 인자로 받아 num = num + 100과 lst.append(0) 실행"""
    num = num + 100
    lst.append(0)

# 함수 호출하여 실행
change_both(n, items)

# n 출력
print(n)
# items 출력
print(items)