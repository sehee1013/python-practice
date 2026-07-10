data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
p = int(input())

# 분할 위치
k = len(data) * p // 100

# 입력 받은 데이터 비율로 train과 val 구분하기
train = " ".join(map(str, data[:k]))
val = " ".join(map(str, data[k:]))


# 결과 출력
print("train: " + train if train else "train:")
print("val: " + val if val else "val:")