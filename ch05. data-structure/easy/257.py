# 슬라이싱 두 조각을 이어 붙이면 그대로 회전이다. 반복문 없이 한 줄로 끝낼 수 있다.
n = int(input())

# n개의 이름 입력 받기
name_list = input().split(" ")

# 정수 k 입력 받기
k = int(input())

# 왼쪽으로 k칸 회전한 명단 한 줄로 출력
moved_list = name_list[k:] + name_list[:k]
print(" ".join(moved_list))