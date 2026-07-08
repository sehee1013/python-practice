# range는 음수 step을 지원합니다. 1 미만으로 내려가지 않도록 종료값을 설정하세요.
n = int(input())
k = int(input())

# n부터 1이상까지 K만큼 감소시켜 출력
for count in range(n, 0, -k):
    
    print(count, end=" ")

# 줄바꿈 후 발사 메시지 출력
print()
print("발사!")