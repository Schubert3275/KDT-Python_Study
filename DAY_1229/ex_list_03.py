# -------------------------------------------------------------------
# list의 원소/요소 데이터 변경 및 삭제
# -------------------------------------------------------------------
# "Merry Christmas"의 문자 1개 1개를 원소로 가지는 리스트로 생성
msgList = list("Merry Christmas")

print(f'msgList => {msgList}')

# => ' ' 데이터를 '***' 변경하기
print(f'msgList[5] => {msgList[5]}')

msgList[5] = '***'
print(f'msgList => {msgList}')

# 삭제 ==> del 데이터 또는 del(데이터) -----------------------------
del msgList[5]
print(f'msgList => {msgList}')

del(msgList[5])
print(f'msgList => {msgList}')

del msgList[::2]
print(f'msgList => {msgList}')

del msgList
