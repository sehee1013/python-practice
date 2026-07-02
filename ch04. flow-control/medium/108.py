# 바깥 for는 각 글자, 안쪽 for는 n번 출력
text = input()
n = int(input())

# text의 모든 글자 출력할 때까지 반복
for char in text:
    # 글자 n번 출력할 때까지 반복
    for _ in range(n):
        print(char, end="")

print()