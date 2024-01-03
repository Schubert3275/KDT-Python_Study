"""
18.5 연습문제: 3으로 끝나는 숫자만 출력하기
"""
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1
