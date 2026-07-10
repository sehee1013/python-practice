data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = int(input())
end = int(input())

# data[a:b] 구간을 단일 원소 [0] 으로 교체
data[start:end] = [0]

# 공백 구분하여 최종 리스트 한 줄에 출력
print(" ".join(map(str, data)))