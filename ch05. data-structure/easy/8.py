# `index` 메서드는 없는 값을 찾으면 오류가 발생하므로, 먼저 `in`으로 존재 여부를 확인하세요.
names = ["윤서", "지우", "민준", "서윤", "도윤", "예준"]
name = input()

# 명단에 있는 경우
if name in names:

    # index() 사용하여 리스트를 순회하여 name의 인덱스 번호 + 1 출력
    print(f"{names.index(name) + 1}번째에 있습니다")

# 명단에 없는 경우 경고 메시지 출력
else:
    print("명단에 없습니다")