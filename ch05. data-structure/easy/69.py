# 항목 삭제는 `del d[key]` 또는 `d.pop(key)` 로 가능합니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 입력 받은 학생 이름이 scores 딕셔너리에 있으면 제거, 없으면 경고 메시지 출력 후 종료
if name in scores:
    scores.pop(name)
else:
    print("해당 학생은 존재하지 않습니다")
    exit()

# 결과 출력
for std_name, score in scores.items():
    print(f"{std_name}: {score}")