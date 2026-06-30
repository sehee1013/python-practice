# 바깥 for문으로 줄, 안쪽 for문으로 별 개수를 제어하세요.
num = int(input())

# 1번째 줄에 별 1개, 2번째 줄에 별 2개씩 출력해서 삼각형 만들기
for star in range(num):
    print("*" * (star + 1)) 