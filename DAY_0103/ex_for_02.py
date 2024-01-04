# ---------------------------------------------------
# [실습1] 'Hello World' 100번 출력
# ---------------------------------------------------
# 반복문 => for in 반복문 =============================
# - 여러개의 데이터를 가지고 있는 데이터에서 한 개씩 원소/요소를
#   읽어와줌
# for 요소저장변수명 in 여러개 데이터 가진 타입:
# <---->요소/원소 반복할 코드
# <---->요소/원소 반복할 코드
# ---------------------------------------------------
msg = "Happy New Year 2024! Good Luck^^"

# msg를 구성하는 문자 한개씩 화면에 한 줄에 한 개씩 출력해주세요!
print(msg[0])  # H
print(msg[1])  # a
print(msg[2])  # p
print(msg[3])  # p
print(msg[4])  # y
print(msg[5])  #
print(msg[6])  # N
print(msg[7])  # e

for ele in msg:
    print(ele)

# [실습1] 'Hello World' 100번 출력
for cnt in range(100):
    print("Hello World")

# [실습2] 좋아하는 음식명을 리스트에 저장하기 (단, 10개 )
foods = ['떡볶이', '순대', '돈까스', '치즈', '찜닭', '닭발', '족발', '짜장면', '짬뽕', '탕수육']

print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])
print(foods[4])
print(foods[5])
print(foods[6])
print(foods[7])
print(foods[8])
print(foods[9])

for cnt in foods: print(cnt)

for cnt in foods:
    print(cnt)

for key, value in enumerate(foods):
    print(key, value) # 인덱스 키값

print("=" * 30)

for key, value in enumerate(foods):
    print(key, value) # 인덱스 키값

print("=" * 30)

for key, value in enumerate(foods):
    print(key, value) # 인덱스 키값

print("=" * 30)

sample = enumerate(foods)
next(sample)  # (0, 7)
next(sample)  # (1, 9)
next(sample)  # (0, 7)
next(sample)  # (1, 9)
next(sample)  # (0, 7)
next(sample)  # (1, 9)
next(sample)  # (0, 7)
next(sample)  # (1, 9)
next(sample)  # (0, 7)
next(sample)  # (1, 9)
next(sample)  # (0, 7)
next(sample)  # (1, 9)
