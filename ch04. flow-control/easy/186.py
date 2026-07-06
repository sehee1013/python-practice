# 총 초를 입력받아 HH:MM:SS 형식으로 출력하세요.
total_seconds = int(input())

# 시 구하기
hours = total_seconds // 3600
total_seconds %= 3600

# 분 구하기
minutes = total_seconds // 60
total_seconds %= 60

# 초 구하기
seconds = total_seconds

# 결과 출력하기
print(f"{hours:02}:{minutes:02}:{seconds:02}")