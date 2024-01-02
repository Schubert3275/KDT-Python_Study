"""
13.6 연습문제: if 조건문 사용하기
"""
x = 5
if x != 10:
    print('ok')
print('-' * 50)

"""
13.7 심사문제: 온라인 할인 쿠폰 시스템 만들기
"""
price = int(input())
coupon = input()
if coupon == 'Cash3000':
    print(price - 3000)
if coupon == 'Cash5000':
    print(price - 5000)
print('-' * 50)

"""
14.6 연습문제: 합격 여부 판단하기
"""
written_test = 75
coding_test = True
if written_test >= 80 and coding_test == True:
    print('합격')
else:
    print('불합격')
print('-' * 50)

"""
14.7 심사문제: 합격 여부 판단하기
"""
point = list(map(int, input().split()))
if 0 <= point[0] <= 100 and 0 <= point[1] <= 100 and 0 <= point[2] <= 100 and 0 <= point[3] <= 100:
    if sum(point) / 4 >= 80:
        print("합격")
    else:
        print("불합격")
print('-' * 50)

"""
15.3 연습문제: if, elif, else 모두 사용하기
"""
x = int(input())

if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')
print('-' * 50)

"""
15.4 심사문제: 교통카드 시스템 만들기
"""
age = int(input())
balance = 9000
if 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
else:
    balance -= 1250
print(balance)
print('-' * 50)
