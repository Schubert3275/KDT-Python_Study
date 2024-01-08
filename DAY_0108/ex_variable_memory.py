num = 10
print(f'num => {id(num)}, {type(num)}')

num = 10.5
print(f'num => {id(num)}, {type(num)}')

num = 'Good'
print(f'num => {id(num)}, {type(num)}')

num1 = []
print(f'num1 => {id(num1)}, {type(num1)}')

num2 = [11, 22.1]
print(f'num2 => {id(num2)}, {type(num2)}')
print(f'num2[0] => {id(num2[0])}, {type(num2[0])}')
print(f'num2[1] => {id(num2[1])}, {type(num2[1])}')

print("\n=================== 값 변경 ====================\n")
num = 'Happy'
print(f'num => {num} : {id(num)}, {type(num)}')

num2[0] = 100
print(f'num2 => {id(num2)}, {type(num2)}')
print(f'num2[0] => {id(num2[0])}, {type(num2[0])}')
