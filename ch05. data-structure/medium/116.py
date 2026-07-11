text = input()
n = int(input())

# text 공백 기준으로 구분하여 단어 리스트 생성
words = text.split()

# n이 단어 개수 초과하면 '없음' 출력
if n > len(words):
    print('없음')
# 아니면 n번째 단어 출력
else:
    print(words[n - 1])