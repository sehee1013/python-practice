# 위 수식 그대로, 플레이어 선공 → 몬스터 사망 확인 → 몬스터 공격 → 플레이어 사망 확인
player_hp = 100
monster_hp = 80
turn = 0
print("=== RPG 전투 시작! ===")
print("플레이어 HP:", player_hp, "| 몬스터 HP:", monster_hp)
print()

# 출력 함수
def player_attack(turn, damage, monster_hp):
    print(f"--- {turn}턴 ---")
    print(f"플레이어 공격! 데미지: {damage} | 몬스터 HP: {monster_hp}")

def monster_attack(damage, player_hp):
    print(f"몬스터 공격! 데미지: {damage} | 플레이어 HP: {player_hp}")
    print()

while True:
    # 턴 + 1
    turn += 1
    # 데미지 계산
    player_damage = 15 + (turn * 7 + 3) % 11
    monster_damage = 10 + (turn * 11 + 5) % 11

    # 몬스터 hp 갱신
    monster_hp -= player_damage

    # 플레이어 공격 상황 출력
    player_attack(turn, player_damage, monster_hp)
    
    # 몬스터 hp가 0 이하면 즉시 종료
    if monster_hp <= 0:
        break

    # 몬스터 반격
    player_hp -= monster_damage
    monster_attack(monster_damage, player_hp)

    # 플레이어 hp가 0 이하면 즉시 종료
    if player_hp <= 0:
        break

# 결과 출력
if monster_hp <= 0:
    print()
    print(f"플레이어 승리! ({turn}턴 만에 승리)")
else:
    print("몬스터 승리... (플레이어 패배)")