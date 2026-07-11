text = input()
target = input()

# 본문에 타겟이 있는지 검사
if target in text:
    # 찾아서 인덱스 출력
    print(text.index(target))
# 없는 경우 없음 메시지 출력
else:
    print("없음")