scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())
count = 0

# 딕셔너리의 값(value) 순회하기
for score in scores.values():
    # cutoff 이상이면 count + 1
    if score >= cutoff:
        count += 1

# 결과 출력
print(count)