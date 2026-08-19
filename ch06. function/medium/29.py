# 흐름: 입력 읽기 -> 함수 호출 -> 함수 실행 결과 출력
raw = input().split()
base = int(raw[0])
extra = {}
for t in raw[1:]:
    k, v = t.split("=")
    extra[k] = int(v)

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def merge(base, **extra):
    total = base
    for k in extra:
        total += extra[k]
    return total

# 함수 호출하여 실행 결과 출력하기
print(merge(base, **extra))