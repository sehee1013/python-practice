text = input()
new_sep = input()

# ,로 구분된 문자열을 리스트로 변환
parts = text.split(",")

# new_sep을 구분자로 한 줄 출력
print(new_sep.join(parts))