# f-string `:+.1f` 로 부호 포함 소수점 포맷. 등수는 자신보다 큰 점수 수 + 1.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

if name in scores:
    # 조회 학생 점수
    target_score = scores[name]
    # 평균 구하기
    average = sum(scores.values()) / len(scores)

    rank = 1

    # 등수 구하기
    for score in scores.values():
        if score > target_score:
            rank += 1

    # 이름 출력
    print(f"이름: {name}")
    # 점수 출력
    print(f"점수: {target_score}")
    # 평균 차이 출력
    print(f"평균 차이: {(target_score - average):+.1f}")
    # 등수 출력
    print(f"등수: {rank}등")
    
# 해당 학생이 없으면 '학생 없음' 출력
else:
    print("학생 없음")