count = int(input())
total = 1

# count 수 만큼 정수 입력받고 모든 숫자의 곱 출력하기
for i in range(0, count):
    num = int(input())
    total *= num

print(f"누적 곱: {total}")    