# for i in range(len(text)): 조건 만족 시 출력 후 break. found 플래그로 미발견 처리.
text = "hello python"
target = "p"

# 아직 못 찾은 상태
found = False
# 문자열에서 타겟 찾기
for i in range(len(text)):
    if text[i] == target:
        # 타켓 인덱스 번호랑 같이 출력
        print(f"'{target}'을(를) {i}번째 위치에서 찾았습니다!")
        found = True #타겟 찾음
        break


# 타겟 찾지 못한 경우 메시지 출력
if not found:
    print("찾지 못했습니다") 