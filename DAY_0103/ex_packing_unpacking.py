# ---------------------------------------------------------
# 팩킹(Packing) & 언팩킹(Unpacking)
# ---------------------------------------------------------
msg = "Happy New Year"

# 팩킹(Packing) 방식
msgList = msg.split()
print(msgList[0], msgList[-1])

# 언팩킹(Unpacking) 방식-----------------------------------
# 데이터수와 변수 수가 동일 해야함!!!
m1, m2, m3 = msg.split()
print(m1, m2, m3)

# 데이터와 변수 수가 달라서 Error 발생
# m1, m2=msg.split()
# print(m1, m2)

# 변수를 여러 개 생성하는 경우 ----------------------------
age = 12
name = "Hong"
job = '학생'

# 튜플을 언팩킹으로 생성 가능
info = (12, 'Hong', '학생')
info2 = 12, 'Hong', '학생'
age1 = info2[0]
name1 = info2[1]
job1 = info2[2]

age1, name1, job1 = 12, 'Hong', '학생'


def myFunc(a, b):
    return a+b, a-b, a*b, a/b if not b else -1


result = myFunc(10, 3)
print(f'덧셈 결과 :{result[0]}, 뺄셈 결과 : {result[1]}, 곱셈 결과 : {result[2]}, 나눗셈 결과 : {result[3]}')

plus, minus, multi, div = myFunc(10, 3)
print(f'덧셈 결과 :{plus}, 뺄셈 결과 : {minus}, 곱셈 결과 : {multi}, 나눗셈 결과 : {div}')