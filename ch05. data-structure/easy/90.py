datasets = [
    ["apple", "banana", "apple", "cherry"],
    [1, 2, 1, 2, 1, 2, 3],
    ["A", "B", "C", "D", "E"]
]
t = int(input())

# 결과 출력
print(len(set(datasets[t])))