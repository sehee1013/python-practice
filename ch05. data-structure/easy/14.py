# 두 함수 호출만으로 한 줄씩 출력하면 됩니다.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 40],
    [42],
]
t = int(input())
scores = data_sets[t]

# max(), min() 사용하여 최댓값과 최솟값 반환하여 출력
print(f"최고: {max(scores)}")
print(f"최저: {min(scores)}")