numbers = {1, 5, 3, 8, 2, 10, 7, 4}
cutoff = int(input())

# cutoff 이상의 원소인 경우 정렬하여 리스트에 추가
result = sorted([num for num in numbers if num >= cutoff])

# 결과 출력
print(" ".join(map(str, result)))