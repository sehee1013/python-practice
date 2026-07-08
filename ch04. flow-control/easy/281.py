# 끝값은 포함되지 않는 점에 유의해 for 반복문을 작성하세요.
start = int(input())
stop = int(input())
step = int(input())

# start부터 stop까지 step씩 증가하며 출력
print(" ".join(map(str, range(start, stop, step))))