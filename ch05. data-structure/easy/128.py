scores = [85, 92, 65, 78, 95]
cutoff = int(input())

# cutoff 이상이면 count + 1
count = sum(1 for score in scores if score >= cutoff)

# 결과 출력
print(count)