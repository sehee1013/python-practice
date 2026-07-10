# step 인자에 2를 주면 짝수 인덱스만 선택됩니다.
data_sets = [
    [10, 11, 20, 21, 30, 31, 40, 41, 50, 51],
    [1, 2, 3, 4, 5],
    [100],
]
t = int(input())
data = data_sets[t]

# 짝수 인덱스 추출 후 출력
print(" ".join(map(str, data[::2])))