# 사본을 만든 후 사본에만 정렬을 적용해야 원본이 보존됩니다.
data_sets = [
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
    [5, 3, 1],
    [7],
]
t = int(input())
original = data_sets[t]

# 새 리스트 생성
copy_data = original[:]
# 새 리스트 정렬
copy_data.sort()

# 결과 출력
print("원본: " + " ".join(map(str, original)))
print("정렬: " + " ".join(map(str, copy_data)))
print("원본: " + " ".join(map(str, original)))