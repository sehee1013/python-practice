# 리스트에 같은 값이 몇 개인지 셀 때는 count 메서드가 편리합니다.
scores = [85, 92, 78, 85, 88, 85, 100, 65, 82, 90]
score = int(input())

# 리스트 안 입력 받은 정수 X의 개수 세고 출력
print(scores.count(score))