# start=1, step=2 슬라이스로 홀수 인덱스만 선택.
data_sets = [
    [10, 11, 20, 21, 30, 31, 40, 41, 50, 51],
    [1, 2, 3, 4, 5],
    [100],
]
t = int(input())
data = data_sets[t]

# 홀수 번호 인덱스 원소만 추출해서 출력
print(" ".join(map(str, data[1::2])))