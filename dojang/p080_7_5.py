"""
7.5 심사문제: 날짜와 시간 출력하기
"""
year, month, day, hour, minute, second = input().split()

print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')
