# 물통에 물을 순서대로 부어 넘치는 시점을 찾으세요.
c, n = map(int, input().split())
count = 0
total = 0

# n번 입력 받을 때까지 반복
for _ in range(1, n + 1):
    # 물 양 입력 받고 count + 1, total에 입력 받은 물 양 더하기
    water = int(input())
    count += 1
    total += water
    
    # total > c가 되면 그때의 count를 over_count에 저장
    if total > c:
        break

# total > c인 경우 몇 번째 넘쳤는지, 넘친 양 출력
if total > c:
    print(f"{count}번째에서 넘침! 넘친 양: {total - c}")
# 아닌 경우 안 넘침 메시지 출력
else:
    print("안 넘침")