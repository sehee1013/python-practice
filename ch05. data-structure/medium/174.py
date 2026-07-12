from collections import defaultdict
n = int(input())

# 값이 없는 경우 빈 리스트 생성
domains = defaultdict(list)

# n번 이메일 입력 받기
for _ in range(n):
    # '@' 기준으로 구분하여 입력 받기
    name, domain = input().split('@')
    
    # 딕셔너리에 추가
    domains[domain].append(name)
    

# 도메인 정렬하여 출력
for key in sorted(domains):
    print(f"{key}: {' '.join(domains[key])}")