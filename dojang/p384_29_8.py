"""
29.4 심사문제: 사칙 연산 함수 만들기
"""
x, y = map(int, input().split())


def calc(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2 if num2 else 0


#

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
