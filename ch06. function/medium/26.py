# 흐름: 입력 읽기 -> 함수 호출 -> 함수 실행 결과 출력
parts = input().split()
text = parts[0]
start = int(parts[1])
end = int(parts[2])

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def slice_text(text, *, start, end):
    return text[start:end]

# 함수 호출하여 실행 결과 출력
print(slice_text(text, start=start, end=end))