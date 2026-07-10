# 이미 있는 키에 다시 대입하면 값이 갱신됩니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()
new_score = int(input())

# 입력 받은 이름이 딕셔너리에 있는 경우
if name in scores:
    # 입력 받은 점수로 키값 수정
    scores[name] = new_score
else:
    print("해당 이름의 학생은 존재하지 않습니다.")
    exit()
# 결과 출력
print(f"{name}: {scores[name]}")