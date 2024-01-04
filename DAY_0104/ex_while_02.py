# -----------------------------------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해진 경우에도 사용 가능함
# -----------------------------------------------------------------------------
# [요청] 사용자가 알고 싶어하는 단을 입력 받아서 해당 단의 구구단을 출력
#        단, while 반복문 사용하기
# [예시] 알고 싶은 단 입력 : 3
#        -- 3단 --
#        3 * 1 = 3
#        3 * 2 = 6
#        3 * 3 = 9
#        3 * 4 = 12
#        3 * 5 = 15
#        3 * 6 = 18
#        3 * 7 = 21
#        3 * 8 = 24
#        3 * 9 = 27
# -----------------------------------------------------------------------------
TEST = False, True

if TEST[0]:
    dan = int(input("알고 싶은 단 입력: "))
    num = 0
    while num < 10:
        if num:
            print(f'{dan} * {num} = {dan*num:<2}')
        else:
            print(f'--- {dan}단 ---')
        num += 1

# -----------------------------------------------------------------------------
# [요청] 2단 ~ 9단 출력 단, while 반복문 사용
#        -- 2단 --
#        2 * 1 = 2
#        2 * 2 = 4
#        2 * 3 = 6
#            :
#        -- 3단 --
#        3 * 1 = 3
#        3 * 2 = 6
#        3 * 3 = 9
#            :
#        -- 9단 --
#        9 * 1 = 9
#        9 * 2 = 18
#        9 * 3 = 27
#            :
#        9 * 9 = 81
# -----------------------------------------------------------------------------
if TEST[1]:
    dan, unit = 2, '단'
    while dan < 10:
        print(f'{str(dan)+unit:-^10}')
        num = 1
        while num < 10:
            print(f'{dan} * {num} = {dan * num:<2}')
            num += 1
        dan += 1