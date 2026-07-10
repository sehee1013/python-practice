# 빈 set 은 `set()` 으로 만든다는 점이 중요.
data_sets = [
    {"apple", "banana", "cherry", "date"},
    {"single"},
    set(),
]
t = int(input())
fruits = data_sets[t]

# 결과 출력
print(len(fruits))