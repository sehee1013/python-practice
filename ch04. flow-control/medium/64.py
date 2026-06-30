# chr(65)는 'A', chr(65+1)은 'B'입니다.
n = int(input())

#N번 행 출력, 첫번째 행 1개, 마지막 행 알파벳 N개 출력
for row in range(n):
    for alpha in range(row + 1):
        print(chr(65 + alpha), end = "")
    print() # 줄바꿈