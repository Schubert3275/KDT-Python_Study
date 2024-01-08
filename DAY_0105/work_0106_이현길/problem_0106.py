# -------------------------------------------------------------------------------------------------
# 1. 문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을
#    출력하는 함수를 구현하세요.
# -------------------------------------------------------------------------------------------------
def funcStrSorting(msg: list):
    msg.sort(reverse=True)
    print(f'정렬 결과: {msg}')
    print(f'가장 높은 문자열: {msg[0]}, 가장 낮은 문자열: {msg[-1]}')


# -------------------------------------------------------------------------------------------------
# 2. 키보드로 입력 받은 데이터 중에서 숫자만 모두 저장하여 합계, 최대값, 최소값을
#    출력하는 함수를 구현하세요.
# -------------------------------------------------------------------------------------------------
def funcSumMaxMin():
    # 하늘 Apple 2021 -9 False 23 7 None 끝
    # A 홍길동 False True True None Good Luck 가나다라
    dataList = input("데이터 입력: ").split()
    numList = []
    for data in dataList:
        data_check = data.replace('-', '')
        if data_check.isdecimal():
            numList.append(int(data))
    if len(numList) == 0:
        numList.append(0)
    print(f'합계: {sum(numList)}, 최댓값: {max(numList)}, 최솟값: {min(numList)}')


# -------------------------------------------------------------------------------------------------
# 3. 아래 조건을 만족하는 코드를 작성하세요.
# -------------------------------------------------------------------------------------------------
def funcPrintPattern():
    while True:
        inputData = input("알파벳 혹은 숫자를 입력하세요.\n종료하려면 'q' 또는 'Q'를 입력합니다: ")
        if len(inputData) == 1:
            if inputData in ('q', 'Q'):
                break
            elif inputData.isdecimal():
                print('◎' * int(inputData))
            elif inputData.isupper():
                print('♠')
            elif inputData.islower():
                print('♤')
            else:
                print("올바르지 않은 입력입니다.")
        else:
            print("한 글자만 입력해 주세요.")
        print()


# -------------------------------------------------------------------------------------------------
# 4. 아래 조건을 만족하는 코드를 작성하세요.
# -------------------------------------------------------------------------------------------------
def funcCommonMult():
    threeSet = {i for i in range(3, 101, 3)}
    sevenSet = {i for i in range(7, 101, 7)}
    eightSet = {i for i in range(8, 101, 8)}
    commonList = sorted(threeSet | sevenSet | eightSet)
    print(commonList)


# -------------------------------------------------------------------------------------------------
# 5. 문자열을 입력하면 코드값을 아래와 같이 출력해주는 함수를 구현해 주세요.
# -------------------------------------------------------------------------------------------------
def funcEncoding(data: str):
    hexEncoding = ''
    binEncoding = ''
    for letter in data:
        hexEncoding += hex(ord(letter))
        binEncoding += bin(ord(letter))
    print(f'"{data}"의 인코딩: {hexEncoding}')
    print(f'"{data}" 인코딩: {binEncoding}')


# -------------------------------------------------------------------------------------------------
# 6. 문자열 리스트와 정수 1개를 입력하면 아래와 같이 출력하는 함수를 구현해 주세요.
# -------------------------------------------------------------------------------------------------
def strIndexSorting(datas: list, n: int):
    if len(datas) > n:
        sortDatas = sorted(datas, key=lambda x: x[n])
        return sortDatas
    else:
        print(f'문자열의 길이가 {n} 보다 커야 합니다.')
        return -1


# -------------------------------------------------------------------------------------------------
# 7. 아래와 같이 출력되는 함수를 구현해 주세요.
# -------------------------------------------------------------------------------------------------
def funcContinuousTwo(nums: list):
    continuousList = []
    if nums.count(2) >= 2:
        start = nums.index(2)
        end = nums[::-1].index(2)
        continuousList = nums[start:-end]
    elif nums.count(2) == 1:
        continuousList.append(2)
    else:
        continuousList.append(-1)
    return continuousList


# -------------------------------------------------------------------------------------------------
# 8. 아래와 같이 출력된 함수를 구현해 주세요.
# -------------------------------------------------------------------------------------------------
def funcSumZero(nums: list):
    combiSet = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i >= j:
                continue
            for k in range(len(nums)):
                if i >= k or j >= k:
                    continue
                if (nums[i] + nums[j] + nums[k]) == 0:
                    combiSet.add(frozenset({nums[i], nums[j], nums[k]}))
    print(len(combiSet))


# -------------------------------------------------------------------------------------------------
# 9. 아래와 같이 출력된 함수를 구현해 주세요.
# -------------------------------------------------------------------------------------------------
def funcMultiTable(dan: int):
    danStr = f' {dan}단 '
    tables = [f'{dan} * {i} = {dan * i:>2}' for i in range(1, 10)]
    print(f'{danStr:-^41}')
    for idx, table in enumerate(tables, 1):
        print(table, end='\t\t' if idx % 3 else '\n')


# -------------------------------------------------------------------------------------------------
# 10. 숫자와 콤마로만 이루어진 문자열 data가 주어지면 이때, data에 포함되어있는 자연
#     수의 합과 가장 작은 수, 가장 큰 수를 출력하는 함수를 구현하세요.
# -------------------------------------------------------------------------------------------------
def funcSumMaxMin2(data: str):
    dataFix = data.replace(',', '')
    numList = [int(i) for i in dataFix]
    print(f'"{data}"의 합: {sum(numList)}, 가장 큰 수: {max(numList)}, 가장 작은 수: {min(numList)}')


# -------------------------------------------------------------------------------------------------
# 11. 업-다운 빙고 게임 기능의 함수를 구현하세요.
# -------------------------------------------------------------------------------------------------
def funcBingo():
    from random import randint
    randNum = randint(1, 100)
    while True:
        guessNum = int(input("빙고 넘버: "))
        if guessNum > randNum:
            print(f'힌트 - {guessNum}보다 작은 수')
        elif guessNum < randNum:
            print(f'힌트 - {guessNum}보다 큰 수')
        else:
            print("정답 - *~ 빙고 ~*")
            break


# -------------------------------------------------------------------------------------------------
# 12. 2, 4, 8 게임은 숫자의 끝 자리가 2, 4, 8로 끝나는 숫자의 경우 다른 문자로 출력하는
#     게임으로 아래 조건을 만족하도록 구현하자.
# -------------------------------------------------------------------------------------------------
def func248game():
    gameNum = int(input("게임 정수 입력: "))
    numList = ['#' if i % 10 == 2 or i % 10 == 4 or i % 10 == 8 else i for i in range(1, gameNum + 1)]
    for idx, num in enumerate(numList, 1):
        print(num, end='' if idx % 20 else '\n')


# -------------------------------------------------------------------------------------------------
# 13. 월(Month)을 입력 받아 해당 월(Month)의 영어와 계절을 출력하는 코드를 작성하세요.
# -------------------------------------------------------------------------------------------------
def funcMonth():
    monthNum = tuple(str(i) for i in range(1, 13))
    monthEng = ('January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December')
    seasons = ('Winter', 'Winter', 'spring', 'spring', 'spring', 'summer',
               'summer', 'summer', 'fall', 'fall', 'fall', 'Winter')
    monthDic = dict(zip(monthNum, zip(monthEng, seasons)))
    month = input("좋아하는 월 입력: ")
    if month in monthDic:
        print(monthDic[f'{month}'][0], monthDic[f'{month}'][1])
    else:
        print("존재하지 않는 월입니다.")


# -------------------------------------------------------------------------------------------------
# 14. 숫자와 화폐단위 입력 받아 세자리 마다 쉼표(,) 찍어서 출력하는 기능을 구현하세요.
# -------------------------------------------------------------------------------------------------
def funcExpression(moneyStr: str):
    money, unit = moneyStr.split(',')
    money = int(money.strip())
    unit = unit.strip()
    print(f'{money:,}{unit}')


# -------------------------------------------------------------------------------------------------
# 15. 입력받은 숫자 월(Month)에 대한 영어와 한국어 표기를 출력하는 함수를 구현하세요.
# -------------------------------------------------------------------------------------------------
def funcMonth2():
    monthNum = tuple(str(i) for i in range(1, 13))
    monthEng = ('January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December')
    seasons = ('일월', '이월', '삼월', '사월', '오월', '유월',
               '칠월', '팔월', '구월', '시월', '십일월', '십이월')
    monthDic = dict(zip(monthNum, zip(monthEng, seasons)))
    month = input("좋아하는 월 입력: ")
    if month in monthDic:
        print(monthDic[f'{month}'][0], monthDic[f'{month}'][1])
    else:
        print("존재하지 않는 월입니다.")


# -------------------------------------------------------------------------------------------------
# 16. 입력받은 정수 2개에 대한 공약수를 모두 출력하는 함수를 만들어 주세요.
# -------------------------------------------------------------------------------------------------
def funcCommonDiv():
    num1, num2 = map(int, input("약수 구하고 싶은 수: ").split())
    commonNum = []
    for idx in range(1, min(num1, num2)+1):
        if num1 % idx == 0 and num2 % idx == 0:
            commonNum.append(idx)
    print(f'{num1}, {num2}의 공약수:', ', '.join(map(str, commonNum)))


# -------------------------------------------------------------------------------------------------
# 17. 입력 받은 메시지 중에서 중복 없이 숫자만 출력하는 함수를 만들어 주세요.
# -------------------------------------------------------------------------------------------------
def funcDuplicat(msg: str):
    numList = []
    for s in msg:
        if s.isdecimal() and s not in numList:
            numList.append(s)
    print(', '.join(map(str, numList)))


# -------------------------------------------------------------------------------------------------
# 18. 생일을 입력 받은 후 한국 나이, 만 나이를 알려주는 함수를 생성해 주세요.
# -------------------------------------------------------------------------------------------------
def funcHowOld(birth: str):
    from time import localtime
    timeNow = localtime()
    birthFix = tuple(map(int, birth.split('.')))
    age = timeNow[0] - birthFix[0]
    print(f'당신의 한국 나이는 {age + 1}세입니다.')
    if birthFix[1] > timeNow[1] or birthFix[1] == timeNow[1] and birthFix[2] > timeNow[2]:
        age -= 1
    print(f'당신의 만 나이는 {age}세입니다.')


# -------------------------------------------------------------------------------------------------
# 19. 팩토리얼(Factorial)을 while 반복문으로 구현해 주세요.
#     팩토리얼 수를 입력 받아서 팩토리얼 결과를 아래와 같이 출력하세요.
# -------------------------------------------------------------------------------------------------
def funcFac():
    num = int(input("팩토리얼 수 입력: "))
    if num > 0:
        facStr = ''
        facNum = 1
        loopNum = num
        while loopNum > 0:
            facNum *= loopNum
            facStr += str(loopNum) + (' * ' if loopNum > 1 else f' = {facNum}')
            loopNum -= 1
    else:
        facStr = '0'
    print(f'{num}! => {facStr}')


# -------------------------------------------------------------------------------------------------
# 20. 입력받은 숫자 범위 안에서 소수(prime Number)를 찾아서 반환하는 함수를 생성
#     하세요.
# -------------------------------------------------------------------------------------------------
def funcPrimeNumber(num: int):
    primeList = [i for i in range(2, num+1)]
    for i in range(2, num+1):
        for j in range(2, num+1):
            if i != j and i % j == 0:
                primeList.remove(i)
                break
    print(primeList)


# -------------------------------------------------------------------------------------------------
# 21. 아래 데이터를 저장합니다. 그리고 과목별 최고점수, 최저점수를 출력하세요.
# -------------------------------------------------------------------------------------------------
def funcScore():
    scoreDict = {'배트맨': {'국어': 90, '수학': 89, '윤리': 98, '국사': 99},
                 '마징가': {'국어': 82, '수학': 71, '윤리': 80, '국사': 91},
                 '슈퍼맨': {'국어': 77, '수학': 100, '윤리': 92, '국사': 90},
                 '슈렉': {'국어': 94, '수학': 82, '윤리': 93, '국사': 71},
                 '피오나': {'국어': 78, '수학': 99, '윤리': 91, '국사': 83}}
    for subject in '국어', '수학', '윤리', '국사':
        scoreList = []
        for key in scoreDict.keys():
            scoreList.append(scoreDict[key][subject])
        print(f'[{subject}] 최고 점수: {max(scoreList)}, 최저 점수: {min(scoreList)}')


# -------------------------------------------------------------------------------------------------
# 22. 구구단 n단부터 m단까지를 반복문 1개로 구현하는 함수를 생성하세요.
# -------------------------------------------------------------------------------------------------
def funcMultiTable2(startEnd: str):
    start, end = startEnd.split('-')
    start = int(start.strip())
    end = int(end.strip()) + 1
    dan = [f' --[{s}단]--' for s in range(start, end)]
    print('\t\t'.join(dan))
    for i in range(1, 10):
        table = [f'{j} * {i} = {j*i:>2}' for j in range(start, end)]
        print('\t\t'.join(table))


# -------------------------------------------------------------------------------------------------
# 23. 입력받은 숫자 범위 안에서 소수(prime Number)를 찾아서 반환하는 함수를 생성 하세요.
# -------------------------------------------------------------------------------------------------
# 20번 문제와 동일함


# -------------------------------------------------------------------------------------------------
# 24. 입력받은 숫자에서 천자리, 백자리, 십자리, 일자리를 출력하세요.
# -------------------------------------------------------------------------------------------------
def funcDigitNumber(num: int):
    print(f'숫자: {num}')
    print(f'만의 자리: {num // 10000}')
    num1000 = num % 10000
    print(f'천의 자리: {num1000 // 1000}')
    num100 = num1000 % 1000
    print(f'백의 자리: {num100 // 100}')
    num10 = num100 % 100
    print(f'십의 자리: {num10 // 10}')
    num1 = num10 % 10
    print(f'일의 자리: {num1}')


# -------------------------------------------------------------------------------------------------
# 25. 정수, 실수, 논리, 문자열 등 데이터 입력 시 모두 덧셈한 결과 출력하는 함수
#     생성하세요.
# -------------------------------------------------------------------------------------------------
def funcAddData(*args):
    if not args:
        print("None")
    elif type(args[0]) is int:
        print(sum(args))
    elif type(args[0]) is str:
        print(''.join(args))
    elif type(args[0]) is bool:
        print(sum(map(int, args)))


# -------------------------------------------------------------------------------------------------
# 26. 아래 출력결과가 나오도록 코드를 작성하세요.
# -------------------------------------------------------------------------------------------------
def funcStars():
    for i in range(12):
        if i <= 5:
            print(' ' * (6-i) + '*' * (2*i + 1))
        elif 5 < i < 11:
            print(' ' * (i-4) + '*' * (11 - (i-5)*2))
        else:
            print("Good Luck 2023")


# -------------------------------------------------------------------------------------------------
# 27. 문자열 'merry Christmas HaPPy New YEaR'에서 대문자는 소문자로, 소문자는 대문자
#     로 변환하여 출력하는 코드를 구현하세요.
# -------------------------------------------------------------------------------------------------
def funcSwapCase():
    msg = 'Merry Christmas HaPPy New YEaR'
    msgSwap = ''.join([s.upper() if s.islower() else s.lower() for s in msg])
    print(msgSwap)


# -------------------------------------------------------------------------------------------------
# 28. 6가지 연산 결과를 한꺼번에 반환하는 함수를 생성 후 호출하여 결과를 아래와 같이
#     출력해 주세요.
# -------------------------------------------------------------------------------------------------
def funcCalc(num1: int, num2: int):
    print(f'덧셈 결과 : {num1 + num2}')
    print(f'뺄셈 결과 : {num1 - num2}')
    print(f'곱셈 결과 : {num1 * num2}')
    print(f'나눗셈 결과 : {num1 / num2 if num2 else 0}')
    print(f'몫 결과 : {num1 // num2 if num2 else 0}')
    print(f'나머지 결과 : {num1 % num2 if num2 else 0}')


# -------------------------------------------------------------------------------------------------
# 29. 다양한 사람들로부터 개인정보를 입력받는 함수를 구현하세요.
# -------------------------------------------------------------------------------------------------
def funcInfo(**kwargs):
    infoData = '개인정보 : '
    for idx, key in enumerate(kwargs.keys(), 1):
        infoData += f'{key} - {kwargs[key]}' + ('    ' if idx != len(kwargs) else '')
    print(infoData)


# -------------------------------------------------------------------------------------------------
# 30. 생년월일을 입력 받아 별자리를 출력해주는 기능을 구현하세요.
# -------------------------------------------------------------------------------------------------
def funcZodiac():
    birth = input("주민번호 입력(000000-0000000) : ").split('-')[0][2:]
    month = int(birth[:2])
    day = int(birth[2:])
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print("물병자리")
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        print("물고기자리")
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        print("양자리")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        print("황소자리")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        print("쌍둥이자리")
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        print("게자리")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        print("사자자리")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 23):
        print("처녀자리")
    elif (month == 9 and day >= 24) or (month == 10 and day <= 22):
        print("천칭자리")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        print("전갈자리")
    elif (month == 11 and day >= 23) or (month == 12 and day <= 24):
        print("궁수자리")
    else:
        print("염소자리")


# -------------------------------------------------------------------------------------------------
# 31. 입력된 년도가 윤년인지 평년인지 평가하는 코드를 구현하세요.
# -------------------------------------------------------------------------------------------------
def funcLeapYear():
    year = int(input("년도 입력: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'{year}년은 윤년입니다.')
    else:
        print(f'{year}년은 평년입니다.')


# -------------------------------------------------------------------------------------------------
# 32. 아래 조건을 만족하는 함수를 생성 후 코드를 구현해주세요.
# -------------------------------------------------------------------------------------------------
def funcZodiac2(pCode: str):
    from time import localtime
    now = localtime()
    birth, info = pCode.split('-')
    year = int(birth[:2]) + (2000 if int(birth[:2]) < 24 else 1900)
    month = int(birth[2:4])
    day = int(birth[4:])
    genderCheck = info[0]
    cZodiacCheck = year % 12
    cZodiacList = ['원숭이', '닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양']
    age = now[0] - year
    if month > now[1] or (month == now[1] and day > now[2]):
        age -= 1

    if genderCheck in ('1', '3', '9'):
        gender = '남자'
    elif genderCheck in ('2', '4', '0'):
        gender = '여자'
    elif genderCheck in ('5', '7'):
        gender = '외국인 남자'
    else:
        gender = '외국인 여자'

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac = '물병자리'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac = '물고기자리'
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac = '양자리'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac = '황소자리'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        zodiac = '쌍둥이자리'
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        zodiac = '게자리'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac = '사자자리'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 23):
        zodiac = '처녀자리'
    elif (month == 9 and day >= 24) or (month == 10 and day <= 22):
        zodiac = '천칭자리'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        zodiac = '전갈자리'
    elif (month == 11 and day >= 23) or (month == 12 and day <= 24):
        zodiac = '궁수자리'
    else:
        zodiac = '염소자리'
    print(f'{age}세, {gender}, {year}년 {month}월 {day}일 {cZodiacList[cZodiacCheck]}띠 {zodiac}')


def main():
    while True:
        TEST = int(input("확인할 문제 번호를 입력(1-32, 0 또는 범위 외 입력으로 종료) : "))
        print()
        if TEST == 1:    # 1
            print(f'{TEST}번 문제')
            msg17 = ['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']
            funcStrSorting(msg17)
        elif TEST == 2:    # 2
            print(f'{TEST}번 문제')
            # 하늘 Apple 2021 -9 False 23 7 None 끝
            # A 홍길동 False True True None Good Luck 가나다라
            funcSumMaxMin()
        elif TEST == 3:    # 3
            print(f'{TEST}번 문제')
            funcPrintPattern()
        elif TEST == 4:    # 4
            print(f'{TEST}번 문제')
            funcCommonMult()
        elif TEST == 5:    # 5
            print(f'{TEST}번 문제')
            data5 = "가나다"
            funcEncoding(data5)
        elif TEST == 6:    # 6
            print(f'{TEST}번 문제')
            datas6_1 = ['askde', 'beach', 'surf']
            datas6_2 = ['home', 'pitch', 'python']
            print(strIndexSorting(datas6_1, 2))
            print(strIndexSorting(datas6_2, 1))
        elif TEST == 7:    # 7
            print(f'{TEST}번 문제')
            nums7_1 = [0, 1, 2, 4, 5, 2, 9]
            nums7_2 = [0, 1, 2, 4, 5, 2, 9, 3, 2, 8, 1]
            nums7_3 = [0, 1, 2, 4, 5, 3, 1, 7]
            nums7_4 = [0, 0, 0]
            print(funcContinuousTwo(nums7_1))
            print(funcContinuousTwo(nums7_2))
            print(funcContinuousTwo(nums7_3))
            print(funcContinuousTwo(nums7_4))
        elif TEST == 8:    # 8
            print(f'{TEST}번 문제')
            nums8_1 = [-2, 3, 0, 2, -5]
            nums8_2 = [-3, -2, -1, 0, 1, 2, 3]
            funcSumZero(nums8_1)
            funcSumZero(nums8_2)
        elif TEST == 9:    # 9
            print(f'{TEST}번 문제')
            dan9 = int(input("출력 원하는 단 : "))
            funcMultiTable(dan9)
        elif TEST == 10:    # 10
            print(f'{TEST}번 문제')
            data10_1 = '123,42,98,18'
            data10_2 = '1,234'
            funcSumMaxMin2(data10_1)
            funcSumMaxMin2(data10_2)
        elif TEST == 11:    # 11
            print(f'{TEST}번 문제')
            funcBingo()
        elif TEST == 12:    # 12
            print(f'{TEST}번 문제')
            func248game()
        elif TEST == 13:    # 13
            print(f'{TEST}번 문제')
            funcMonth()
        elif TEST == 14:    # 14
            print(f'{TEST}번 문제')
            #      1234567,  $
            # 907, ￦
            money14 = input("숫자 입력: ")
            funcExpression(money14)
        elif TEST == 15:    # 15
            print(f'{TEST}번 문제')
            funcMonth2()
        elif TEST == 16:    # 16
            print(f'{TEST}번 문제')
            funcCommonDiv()
        elif TEST == 17:    # 17
            print(f'{TEST}번 문제')
            # Happy New Year 2023!
            # 홍길동 010-1111-2222
            msg17 = input("메시지 입력: ")
            funcDuplicat(msg17)
        elif TEST == 18:    # 18
            print(f'{TEST}번 문제')
            birth18 = input("생년월일 입력(2000.04.01): ")
            funcHowOld(birth18)
        elif TEST == 19:    # 19
            print(f'{TEST}번 문제')
            funcFac()
        elif TEST == 20:    # 20
            print(f'{TEST}번 문제')
            num20 = int(input("범위 숫자 입력: "))
            funcPrimeNumber(num20)
        elif TEST == 21:    # 21
            print(f'{TEST}번 문제')
            funcScore()
        elif TEST == 22:    # 22
            print(f'{TEST}번 문제')
            startEnd22 = input("시작 구구단, 종료 구구단 입력: ")
            funcMultiTable2(startEnd22)
        elif TEST == 23:    # 23  # 20번 문제와 동일함
            print(f'{TEST}번 문제 : 20번 문제와 동일함')
            num23 = int(input("범위 숫자 입력: "))
            funcPrimeNumber(num23)
        elif TEST == 24:    # 24
            print(f'{TEST}번 문제')
            num24 = int(input("숫자 입력: "))
            funcDigitNumber(num24)
        elif TEST == 25:    # 25
            print(f'{TEST}번 문제')
            # 2, 9, 3, 5, 8, 7
            data25 = input("계산하고 싶은 데이터 입력: ").replace(' ', '').split(',')
            if data25[0].isdecimal():
                data25 = tuple(map(int, data25))
            funcAddData(*data25)
            funcAddData()
            funcAddData(1, 3, 5)
            funcAddData(True, True, False, False, True)
            funcAddData('A')
            funcAddData('A', 'BC', 'Good')
        elif TEST == 26:    # 26
            print(f'{TEST}번 문제')
            funcStars()
        elif TEST == 27:    # 27
            print(f'{TEST}번 문제')
            funcSwapCase()
        elif TEST == 28:    # 28
            print(f'{TEST}번 문제')
            num28_1, num28_2 = map(int, input("숫자 2개 입력 (3, 4)").replace(' ', '').split(','))
            funcCalc(num28_1, num28_2)
        elif TEST == 29:    # 29
            print(f'{TEST}번 문제')
            funcInfo(age='12세', id='mm1004', name='마징가')
            funcInfo(phone='010-2222-1111', job='히어로')
            funcInfo(job='학생', loc='대구')
        elif TEST == 30:    # 30
            print(f'{TEST}번 문제')
            # 011010-3234567
            funcZodiac()
        elif TEST == 31:    # 31
            print(f'{TEST}번 문제')
            funcLeapYear()
        elif TEST == 32:    # 32
            print(f'{TEST}번 문제')
            # 011010-3234567
            pCode32 = input("주민번호 입력(000000-0000000): ")
            funcZodiac2(pCode32)
        else:
            break
        print()


if __name__ == '__main__':
    main()
