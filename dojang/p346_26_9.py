"""
26.9 심사문제: 공약수 구하기
"""
num1, num2 = map(int, input().split())

a = set()
b = set()

for i in range(1, num1+1):
    if num1 % i == 0:
        a.add(i)
for i in range(1, num2+1):
    if num1 % i == 0:
        b.add(i)

divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)
