data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = int(input())
w = int(input())

# i번째 원소부터 w개 원소 공백 구분하여 출력
print(" ".join(map(str, data[i:i+w])))