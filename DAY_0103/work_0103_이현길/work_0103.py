"""
16.2.3 숫자를 감소시키기
"""
# range() 인수를 감소시키기
for i in range(10, 0, -1):
    print("Hello, Word!", i)
print('-' * 50)

# range() 함수 결과를 반전
for i in reversed(range(10)):
    print("Hello, Word!", i)
print('-' * 50)

"""
22.5.2 for 반복문과 if 조건문을 여러 번 사용하기
"""
a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)
print('-' * 50)

"""
22.7.4 튜플 표현식 사용하기
"""
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)
print('-' * 50)
