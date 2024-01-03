"""
19.5 연습문제: 역삼각형 모양으로 별 출력하기
"""
# 중첩 for문 사용
for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print('-' * 50)

# 문자열 연산 사용
for i in range(5):
    print(' ' * i, end='')
    print('*' * (5-i))
