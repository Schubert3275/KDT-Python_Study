"""
5.5 연습문제: 아파트에서 소음이 가장 심한 층수 출력하기
"""
distance = int(input("도로와의 거리를 입력하세요: "))
floor = int(0.2467 * distance + 4.159)

print(f'도로와의 거리가 {distance}m 일 때, 소음이 가장 심한 층은 {floor}층입니다.')
