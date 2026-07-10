words = ["apple", "cat", "banana", "fig", "kiwi", "lemon", "pear"]
n = int(input())

# 단어 길이가 n인 경우 리스트 추가 후 공백 구분으로 출력
result = [word for word in words if len(word) == n]

print(" ".join(result))