# 전역 prefix=첫, text=둘째, inner_prefix=셋째. 예: "[G] 제목 [L]" → prefix="[G]", text="제목", inner_prefix="[L]"
parts = input().split()
prefix = parts[0]
text = parts[1]
inner_prefix = parts[2]

# 함수 정의하기
def label():
    """지역변수 prefix 를 inner_prefix 로 두고(전역 prefix 를 가림), prefix + text 를 반환"""
    prefix = inner_prefix
    return prefix + text

# 함수 호출하여 실행 결과 출력
print(label())
# 전역변수 prefix 출력
print(prefix)