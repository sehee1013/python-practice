scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
n = int(input())

# scores 순회하며 각 학생들의 점수 접근
for name, score in scores.items():
    # 각 학생의 점수에 n 더하기 (100 넘기지 않게 하기)
    final_score = min(score + n, 100)
    
    # 결과 출력
    print(f"{name}: {final_score}")