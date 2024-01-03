# -----------------------------------------------------------------------------
# [실습1] 알고 싶은 단을 입력 받고 해당 단을 출력해 주세요.
# - input()
# - 특정 단의 구구단을 출력 => 반복문 사용하기
# -----------------------------------------------------------------------------
# num = input("알고 싶은 단을 입력하세요 : ")
#
# if num.isdecimal():
#     num = int(num)
#     for i in range(2, 10):
#         print(f'{num:2} * {i} = {num*i:2}')
# elif not num:
#     print("입력된 데이터가 없습니다.")
# else:
#     print("정수를 입력해 주세요.")

# -----------------------------------------------------------------------------
# [실습2] 2단 ~ 9단까지 모두 출력 하세요. 반복문 사용하기!!!
# -----------------------------------------------------------------------------
for i in range(10):
    for j in range(2, 10):
        if i:
            print(f' {j} * {i} = {i*j:<2}', end=' │' if j != 9 else '\n')
        else:
            print(f' --[{j} 단]--', end='  ' if j != 9 else '\n')
