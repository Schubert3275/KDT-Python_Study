"""
19.6 심사문제: 산 모양으로 별 출력하기
"""
num = int(input())

# 중첩 for문 사용
for i in range(num):
    for j in range(num*2-1):
        if j < (num-i)-1:
            print(' ', end='')
        elif (num-i)-1 <= j < num+i:
            print('*', end='')
    print()
print('-' * 50)

# 문자열 연산 사용
for i in range(num):
    print(' ' * (num-1 - i), end='')
    print('*' * (i*2 + 1))
