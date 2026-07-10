fruits = {"apple", "banana", "cherry", "date", "fig"}
item = input()

# 입력 받은 단어 제거
fruits.discard(item)

# 정렬하기
sorted_fruits = sorted(fruits)

# 결과 출력
print(" ".join(sorted_fruits))