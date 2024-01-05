# -----------------------------------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수 정해 지지 않은 경우
# -----------------------------------------------------------------------------
# [요청] 사용자가 'x' 입력 전까지 입력받은 데이터를 저장해 주세요.
# => 몇 번 입력할지 알 수 없음 ==> 무한 입력 받기
# => 종료 조건 ==> 사용자 'x' 입력
TEST = False, False, False, True

if TEST[0]:
    while True:
        data = input("저장하고 싶은 데이터 입력 (종료 x): ")
        # 종료 검사  => break : 키워드가 있는 부분에서 바로 반복 종료, 아래 코드 실행 안됨
        # if data.lower() == 'x':
        # if data == 'x' or data == 'X':
        if data in ('x', 'X'):
            break

        print("OK")
    print("프로그램 종료")

# -----------------------------------------------------------------------------
# [요청] 사용자로부터 x/X 입력 전까지 계속 정수를 입력
#        입력받은 정수 만큼 알파벳을 출력
# [예시] 출력 원하는 알파벳 수 입력 : 5
#        abcde
#        출력 원하는 알파벳 수 입력 : 1
#        a
#        출력 원하는 알파벳 수 입력 : 10
#        abcdefghij
#        출력 원하는 알파벳 수 입력 : 27
#        abcdefghijklmnopqrstuvwxyz 종료
#        출력 원하는 알파벳 수 입력 : 1
#        a
#        출력 원하는 알파벳 수 입력 : x
#        종료
# -----------------------------------------------------------------------------
# while True:
#     num = input("출력 원하는 알파벳 수 입력: ")
#
#     # 무한 입력 반복 종료 조건
#     if num in ('x', 'X'):
#         break  # 즉시 종료
#
#     num = int(num)
#     aCode = ord('a')
#     for i in range(num):
#         if i == 26:
#             break
#         print(chr(aCode+i), end='')
#     print()

if TEST[1]:
    while True:
        count = input("출력 원하는 알파벳 수: ")
        # 종료 코드
        if count in ('x', 'X'):
            print("프로그램 종료됩니다.")
            break
        if count.isdecimal():
            count = int(count)
            aCode = ord('A')
            for value in range(count):
                value += aCode
                print(f'value => {value}, {chr(value)}')
                if value == ord('Z'):
                    break
        else:
            print("정확한 데이터가 아닙니다.")
    print("--- 코드 끝 부분 ---")

if TEST[2]:
    isEnd = False

    for n in range(100):
        if isEnd:
            print("프로그램 종료합니다.")
            break
        print(f'out -> {n}')

        for n2 in range(100):
            if n2 > 10:
                isEnd = True
                break
            print(f'in ====> {n2}번째')

if TEST[3]:
    n1, n2 = 0, 0
    while n1 < 100:
        if n2 > 10:
            break
        print(f'out -> {n1}')
        n2 = 0
        while n2 < 100:
            if n2 > 10:
                break
            print(f'in -> {n2} ====> {n2}번째')
            n2 += 1
        n1 += 1
