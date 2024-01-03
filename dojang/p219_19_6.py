"""
19.6 심사문제: 산 모양으로 별 출력하기
"""
num = int(input())

for i in range(num):
    print(' ' * (4 - i), end='')
    print('*' * (i*2 + 1))
