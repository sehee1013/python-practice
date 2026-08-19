# 흐름: 입력 읽기 -> 함수 호출 -> 함수 실행 결과 출력
parts = input().split()
name = parts[0]
level = int(parts[1])

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def tag(name, *, level):
    return "#" * level + name

# 함수 호출하여 실행 결과 출력
print(tag(name, level=level))