# 기존 N명을 받아 리스트에 append 한 뒤, 마지막에 입력된 새 학생을 insert(0, ...) 로 넣으세요.
n = int(input())

# n번 기존 학생 명단 입력 받기
std_list = [input() for _ in range(n)]

# 새로운 학생 이름 입력 받아 명단 맨 앞에 추가
std_list.insert(0, input())

# 최종 명단 공백 한 칸으로 구분해 한 줄 출력
print(" ".join(std_list))