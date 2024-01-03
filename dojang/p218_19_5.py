"""
19.5 연습문제: 역삼각형 모양으로 별 출력하기
"""
for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
