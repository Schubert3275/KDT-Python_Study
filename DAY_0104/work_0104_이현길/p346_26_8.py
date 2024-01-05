"""
26.8 연습문제: 공배수 구하기
"""
a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}

print(a & b)
