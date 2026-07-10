labels = ["cat", "dog", "bird", "fish", "lion"]
n = int(input())

# 키로 이름, 키값으로 인덱스 받아서 딕셔너리 생성
names = { name: idx for idx, name in enumerate(labels[:n])}

# 결과 출력
for name, idx in names.items():
    print(f"{name}: {idx}")