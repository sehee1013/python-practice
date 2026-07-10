# items()로 (이름, 점수)를 순회하면서 일치하는 이름만 모아 출력
scores = {"윤서": 85, "지우": 92, "민준": 85, "서윤": 78, "도윤": 92, "예준": 65}
x = int(input())
# 특정 점수 받은 학생들을 저장할 리스트 생성
matched_std = []

# scores 딕셔너리에서 키와 값 동시에 받기
for name, score in scores.items():
    # 입력 받은 정수 X랑 score 값이 같은 경우   
    if x == score:
        # matched_std 리스트에 추가
        matched_std.append(name)

# 공백 구분해서 한 줄로 출력
if matched_std:
    print(" ".join(matched_std))
else:
    print("없음")