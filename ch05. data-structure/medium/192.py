# 사람1의 일정 개수 n1 입력 받기
n1 = int(input())
# n1번 시간 입력 받기
n1_schedule= {int(input()) for _ in range(n1)}

# 사람2의 일정 개수 n2 입력 받기
n2 = int(input())
# n2번 시간 입력 받기
n2_schedule= {int(input()) for _ in range(n2)}

# 두 집합의 교집합 생성
conflict = n1_schedule & n2_schedule

# 일정 있는 시간 오름차순 정렬하여 공백 구분 한 줄 출력
# 충돌 없으면 '충돌 없음' 메시지 출력
print(" ".join(map(str, sorted(conflict))) if conflict else "충돌 없음")