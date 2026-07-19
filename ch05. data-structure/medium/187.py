first_word = input()
second_word = input()

# 비교하여 결과 출력
result = "anagram" if sorted(first_word) == sorted(second_word) else "아님"

print(result)