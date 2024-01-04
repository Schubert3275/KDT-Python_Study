# -----------------------------------------------------------------------------
# [실습1]  알고 싶은 단을 입력 받고 해당 단을 출력해 주세요.
# - input()
# - 특정 단의 구구단을 출력 => 반복문 사용 하기
# -----------------------------------------------------------------------------
# dan=input("좋아하는 단 입력 : ")
# # if dan:
# #     # 숫자로만 구성되어 있는지
# #     if dan.isdecimal():
# #         dan=int(dan)
# #         for num in range(1,10):
# #             print(f'{dan} * {num} = {dan*num}')
# #     else:
# #         print("숫자만 입력 가능합니다.")
# # else:
# #     print("입력된 데이터가 없습니다.")
#
# if dan.isdecimal():
#     dan=int(dan)
#     for num in range(9,0,-1):
#         print(f'{dan} * {num} = {dan*num}')
# else:
#     print("정확한 데이터가 아닙니다.")

# -----------------------------------------------------------------------------
# [실습2]  2단 ~ 9단까지 모두 출력 하세요. 반복문 사용하기!!!
# - 중첩 for 반복문
# -----------------------------------------------------------------------------
#  dan=3
# for dan in range(2, 10):
#     print(f'---{dan}단---')
#     for num in range(1, 10):
#         print(f'{dan} * {num} = {dan*num}')

# -----------------------------------------------------------------------------
# [실습3]  2단 ~ 9단까지 모두 출력 하세요. 반복문 사용하기!!!
# - 중첩 for 반복문
# -----------------------------------------------------------------------------
# num = 1 ~ 9
for num in range(10):
    for dan in range(2, 10):
        if num:
            print(f'{dan} * {num} = {dan*num}', end='\n' if dan == 9 else '   ')
        else:
            print(f'----{dan}----', end='\n' if dan == 9 else '   ')

# 타이틀 없는 구구단 ----------------------------------------------------------
for num in range(1,10):
    for dan in range(2, 10):
        print(f'{dan} * {num} = {dan*num:<2}', end='\n' if dan == 9 else '   ')

print("*"*50)
for dan in range(2, 10):
    print(f'---{dan}단---', end='\n' if dan == 9 else '   ')

for num in range(1, 10):
    for dan in range(2, 10):
        if num:
            print(f'{dan} * {num} = {dan*num}', end='\n' if dan == 9 else '   ')
        else:
            print(f'---{dan}단---', end='\n' if dan == 9 else '   ')

# -----------------------------------------------------------------------------
# [실습] 2단 ~ 9단까지 모두 출력 하세요. 반복문 사용하기!!!
# -----------------------------------------------------------------------------
for i in range(10):
    for j in range(2, 10):
        if i:
            print(f' {j} * {i} = {i*j:<2}', end=' │' if j != 9 else '\n')
        else:
            print(f' --[{j} 단]--', end='  ' if j != 9 else '\n')