text = input()

# 공백 기준으로 구분하여 리스트 변환
words = text.split()

# 첫 번째 원소를 longest에 넣기
longest = words[0]

# longest 보다 문자열이 길면 longest 갱신
for word in words[1:]:
    if len(word) > len(longest):
        longest = word

# 결과 출력
print(longest)