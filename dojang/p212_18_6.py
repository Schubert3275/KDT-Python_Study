"""
18.6 심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
"""
start, stop = map(int, input().split())

i = start

while True:
    if i > stop:
        break
    if i % 10 == 3:
        i += 1
        continue
    print(i, end=' ')
    i += 1
