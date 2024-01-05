"""
20.7 연습문제: 2과 11의 배수, 공배수 처리하기
"""
for i in range(1, 101):
    if i % 2 == 0 and i % 11 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)
