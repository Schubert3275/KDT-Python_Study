"""
13.7 심사문제: 온라인 할인 쿠폰 시스템 만들기
"""
price = int(input())
coupon = input()

if coupon == 'Cash3000':
    print(price - 3000)
if coupon == 'Cash5000':
    print(price - 5000)
