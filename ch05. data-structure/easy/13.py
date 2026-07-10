# 정렬이 아니라 단순 역순임에 유의.
data_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤", "예준"],
    ["red", "green", "blue"],
    ["혼자"],
]
t = int(input())
names = data_sets[t]

# 슬라이싱해서 리스트 뒤집기
names = names[::-1]

# 출력
print(" ".join(names))