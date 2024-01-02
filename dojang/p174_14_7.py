"""
14.7 심사문제: 합격 여부 판단하기
"""
point = list(map(int, input().split()))

if 0 <= point[0] <= 100 and 0 <= point[1] <= 100 and 0 <= point[2] <= 100 and 0 <= point[3] <= 100:
    if sum(point) / 4 >= 80:
        print("합격")
    else:
        print("불합격")
