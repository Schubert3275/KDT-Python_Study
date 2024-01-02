"""
8.5 심사문제: 합격 여부 출력하기
"""
korean, english, mathematics, science = map(int, input().split())

print(korean >= 90 and english > 80 and mathematics > 85 and science >= 80)
