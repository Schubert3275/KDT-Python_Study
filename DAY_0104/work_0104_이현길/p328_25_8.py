"""
25.8 심사문제: 딕셔너리에서 특정 값 삭제하기
"""
# keys = "alpha bravo charlie delta"
# keys = "alpha bravo charlie delta echo foxtrot golf"
# values = "10 20 30 40"
# values = "30 40 50 60 70 80 90"
keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x.pop('delta')
key = [k for k, v in x.items() if v == 30]
x.pop(key[0])

print(x)
