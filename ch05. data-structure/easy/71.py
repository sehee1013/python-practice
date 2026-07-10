# `d.get(key, 기본값)` 은 키가 없을 때 KeyError 대신 기본값을 반환
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 입력 받은 이름 출력, 기본값: 0
print(scores.get(name, 0))