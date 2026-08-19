# 흐름: 입력 읽기 -> 함수 호출 -> 함수 실행 결과 출력
parts = input().split()
values = parts[:-1]
sep = parts[-1]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def join_all(*values, sep):
    return sep.join(values)

# 함수 호출하여 실행 결과 출력하기
print(join_all(*values, sep=sep))