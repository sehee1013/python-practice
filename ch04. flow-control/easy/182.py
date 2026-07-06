# N을 입력받아 1~N에서 3의 배수, 5의 배수, 공배수 개수를 세어 출력하세요.
n = int(input())

multiple_3_count = n // 3
multiple_5_count = n // 5
multiple_3_and_5_count = n // 15

# 결과 출력
print(f"3의 배수: {multiple_3_count}개")
print(f"5의 배수: {multiple_5_count}개")
print(f"3과 5의 공배수: {multiple_3_and_5_count}개")