"""
20.8 심사문제: 5와 7의 배수, 공배수 처리하기
"""
num1, num2 = map(int, input().split())

if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1, num2+1):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif not i % 5:
        print("Fizz")
    elif not i % 7:
        print("Buzz")
    else:
        print(i)
