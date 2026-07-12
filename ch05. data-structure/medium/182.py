words = input().split()

# 각각의 길이 구해서 리스트 생성
length = [len(word) for word in words]

# 평균 길이 구하기
average = sum(length) / len(length)

# 결과 출력
print(f"평균 길이: {average:.1f}")