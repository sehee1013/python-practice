# 등급별 카운터 5개를 두고 점수별로 분기. 출력 시 카운트가 0이면 라벨 뒤 공백 없이.
scores = list(map(int, input().split()))

grade_counts = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'F': 0,
}

# scores 순회하며 각 점수의 등급 판별
for score in scores:
    # A등급인 경우
    if score >= 90:
        grade_counts['A'] += 1
    # B등급인 경우
    elif score >= 80:
        grade_counts['B'] += 1
    # C등급인 경우
    elif score >= 70:
        grade_counts['C'] += 1
    # D등급인 경우
    elif score >= 60:
        grade_counts['D'] += 1
    # F등급인 경우
    else:
        grade_counts['F'] += 1

# 딕셔너리 순회하며 각 등급 결과 출력
for grade, count in grade_counts.items():
    star = count * '*'
    
    # "*" 출력이 없는 경우는 'grade:' 형식으로 뒤에 공백 생략하고 출력
    print(f"{grade}: {star}" if star else f"{grade}:")