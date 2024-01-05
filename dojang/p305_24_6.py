"""
24.6 심사문제: 높은 가격순으로 출력하기
"""
# prices = 51900;83000;158000;367500;250000;59200;128500;1304000
prices = list(map(int, input().split(';')))
prices.sort(reverse=True)

for price in prices:
    print(f'{price:9,}')
