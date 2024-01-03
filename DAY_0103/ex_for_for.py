# 1~10
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# 1~10 => 데이터
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in nums:
    print(n, end='_' if n != 5 else '\n')
print("END")

print('*')
print('**')
print('***')
print('****')
print('*****')

print('*' * 1)
print('*' * 2)
print('*' * 3)
print('*' * 4)
print('*' * 5)

for num in range(1, 6):
    print('*' * num)

for num in range(6, 0, -1):
    print('*' * num)


numList = [1, 2, 3]
numListiter = iter(numList)

print(type(numListiter), numListiter)

try:
    print(next(numListiter))
    print(next(numListiter))
    print(next(numListiter))
    print(next(numListiter))
except StopIteration:
    print('End of Iterator')
finally:
    print("END")
