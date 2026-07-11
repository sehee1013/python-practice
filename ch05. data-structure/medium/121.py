line = input()

# , 를 기준으로 구분하여 리스트 변환
name, age, score = line.split(",")

# 각각의 값 인덱스 사용하여 출력
print(f"이름: {name}")
print(f"나이: {age}")
print(f"점수: {score}")