"""
TITLE: 숫자 피라미드
DIFFICULTY: medium
TAGS: nested-loop, for, pattern, numbers

DESCRIPTION:
줄 수 N을 입력받아, i번째 줄에 1부터 i까지의 숫자를 이어붙여 출력하는
숫자 피라미드를 출력하시오.

예시:
- 입력: `3` → 출력: `1\n12\n123`
- 입력: `5` → 출력: `1\n12\n123\n1234\n12345`
"""

# print(j, end="")을 사용해 줄바꿈 없이 이어서 출력하세요.
num = int(input())

# 총 num번 행 출력
# i번 째 줄에 i까지의 숫자 출력하고 각 행은 줄바꿈 없이 이어서 출력
for i in range(1, num + 1):
    print("".join(str(j) for j in range(1, i + 1)))