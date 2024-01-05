"""
29.3 연습문제: 몫과 나머지를 구하는 함수 만들기
"""
x = 10
y = 3


def get_quotient_remainder(a, b):
    return a // b, a % b


quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))
