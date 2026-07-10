# 문자열도 시퀀스이므로 `for c in s` 로 한 글자씩 순회할 수 있습니다. 숫자/기호는 upper() 영향을 받지 않습니다.
s = input()

# 문자열 s에서 한 글자씩 가져와 대문자로 변환 후 리스트 저장
result = [char.upper() for char in s]

# 공백 구분하여 출력
print(" ".join(result))