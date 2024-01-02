"""
5.6 심사문제: 스킬 공격력 출력하기
"""
ap = int(input("AP(Ability Power)를 입력하세요: "))
damage = ap * 0.6 + 225
damage = round(damage, 2)

print(f'AP가 {ap}일 때, 스킬 공격력은 {damage}입니다.')
