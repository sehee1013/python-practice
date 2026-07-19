# (`w.lower()`, `w`) tuple 리스트로 sort → 첫 원소가 정렬 키. 결과는 원본 두 번째 원소만 추출.
words = input().split()

# lower 변환, 원본 튜플 리스트 생성
pairs = [(word.lower(), word) for word in words]

# 정렬 후 한 줄로 결과 출력
print(" ".join(word for lower_word, word in sorted(pairs)))