# 흐름: 입력 읽기 → repeat(text, *, times) 호출 → 결과 출력

# 입력에서 text, times 를 읽습니다. 예: "ab 3" → text="ab", times=3
parts = input().split()
text = parts[0]
times = int(parts[1])

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def repeat(text, *, times):
    return text * times

# 함수 호출하기
print(repeat(text, times=times))