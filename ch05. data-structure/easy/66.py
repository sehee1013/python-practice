scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 입력 받은 이름으로 키값 출력
# 입력 받은 이름이 딕셔너리에 없는 경우 기본 메시지 출력
result = scores.get(name)

if result is not None:
    print(result)
else:
    print("이름을 다시 입력해주세요.")