# 중복과 공백 제거해서 입력 받기
text = set(input().split())

# 정렬 후 출력
sorted_text = sorted(text)

# 공백 구분자로 출력하기
print(" ".join(sorted_text))