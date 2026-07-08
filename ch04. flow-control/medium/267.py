# 플레이어 HP와 몬스터 HP를 입력받아 턴제 전투를 시뮬레이션하세요.
player_hp = int(input())
monster_hp = int(input())
turn = 0
player_win = True

# 시작 메시지 출력
print("=== RPG 전투 시작! ===")
print(f"플레이어 HP: {player_hp} | 몬스터 HP: {monster_hp}")
print()

# 무한 반복
while True:

    # turn + 1
    turn += 1

    print(f"--- {turn}턴 ---")

    # 플레이어 공격
    player_damage = 15 + (turn * 7 + 3) % 11
    monster_hp -= player_damage

    print(f"플레이어 공격! 데미지: {player_damage} | 몬스터 HP: {monster_hp}")
    
    # 몬스터 hp가 0 이하면 즉시 종료
    if monster_hp <= 0:
        break

    # 몬스터 공격
    monster_damage = 10 + (turn * 13 + 5) % 11
    player_hp -= monster_damage

    print(f"몬스터 공격! 데미지: {monster_damage} | 플레이어 HP: {player_hp}")
    print()

    # 플레이어 hp가 0 이하면 즉시 종료
    if player_hp <= 0:
        player_win = False
        break

# 결과 출력
if player_win:
    print()
    print(f"플레이어 승리! ({turn}턴 만에 승리)")
else:
    print("몬스터 승리... (플레이어 패배)")