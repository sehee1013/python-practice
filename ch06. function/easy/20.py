# 흐름: 입력 읽기 → power(base, exp=exp) 호출(키워드 전용) → 결과 출력
parts = input().split()
base = int(parts[0])
exp = int(parts[1])

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def power(base, *, exp):
    return base ** exp

# exp=exp 형태로 함수 실행 결과 출력하기
print(power(base, exp=exp))