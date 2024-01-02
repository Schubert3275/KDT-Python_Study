# ---------------------------------------------------------------------------------------
# [실습1] 2개 숫자 데이터 입력 받은 후 2개의 값을 산술 연산 결과를 출력해 주세요.
#         +, -, *, /, //, %, **
#         [출력 예시]  10 + 4 = 14
# ---------------------------------------------------------------------------------------
# num1, num2 = map(int, input("숫자 2개를 입력하세요(공백으로 분리): ").split())
# 입력 => str 타입 => int 타입
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 산술 연산 출력
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')
print('-' * 50)

# ---------------------------------------------------------------------------------------
# [실습2] [실습1]에서 입력 받은 숫자 데이터를 활용하여 비교 연산 결과를 출력하세요.
#         >, <, >=, <=, ==, !=
#         [출력 예시]  10>4   => True
#                      10==4  => False
# ---------------------------------------------------------------------------------------
# 비교 연산 결과 출력
print(f'{num1} > {num2}\t=> {num1 > num2}')
print(f'{num1} < {num2}\t=> {num1 < num2}')
print(f'{num1} >= {num2}\t=> {num1 >= num2}')
print(f'{num1} <= {num2}\t=> {num1 <= num2}')
print(f'{num1} == {num2}\t=> {num1 == num2}')
print(f'{num1} != {num2}\t=> {num1 != num2}')
print('-' * 50)

# ---------------------------------------------------------------------------------------
# [실습3] [실습1]에서 입력 받은 숫자 데이터를 활용하여
#         최대값과 최소값을 추가로 입력 받은 후 논리연산 결과 출력하세요.
#         [출력 예시]  10>4 and 10>최대값  => True
#                      10>4 or 10>최소값  => True
#                      not 10              => False
# ---------------------------------------------------------------------------------------
# max_num, min_num = map(int, input("최대값과 최소값을 입력하세요(공백으로 분리): ").split())
max_num = int(input("최대값을 입력하세요: "))
min_num = int(input("최소값을 입력하세요: "))

# 논리 연산 결과 출력
# and 연산자 => 왼쪽/오른쪽 모두 True인 경우만 True가 됨
print(f'{num1} > {num2} and {num1} > {max_num}\t=> {num1 > num2 and num1 > max_num}')
print(f'{num1} > {num2} and {num1} > {min_num}\t=> {num1 > num2 and num1 > min_num}')

# or 연산자 => 왼쪽/오른쪽 모두 False인 경우만 False가 됨
print(f'{num1} > {num2} or {num1} > {max_num}\t=> {num1 > num2 or num1 > max_num}')
print(f'{num1} > {num2} or {num1} > {min_num}\t=> {num1 > num2 or num1 > min_num}')

# not 연산자 => not 데이터/변수명/연산식
print(f'not {num1} \t\t\t\t=> {not num1}')
