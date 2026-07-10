data_sets = [
    ["red", "green", "blue", "yellow", "purple"],
    ["apple", "banana", "cherry"],
    ["single"],
]
t = int(input())
items = data_sets[t]

# 인덱스와 값 입력하기
result = [f"{idx}:{name}" for idx, name in enumerate(items)]

# 결과 출력
print(*result)