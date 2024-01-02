"""
1. 아래에 데이터를 저장하는 코드를 작성하세요.
"""
# ① ‘kim1234@naver.com’ 데이터에서 @ 앞부분만 출력하세요
e_mail = 'kim1234@naver.com'
print(f'@ 앞부분: {e_mail[:7]}')
print('-' * 50)

# ② ‘http://www.naver.com’ 데이터에서 도메인 이름만 출력하세요.
address = 'http://www.naver.com'
print(f'도메인 이름: {address[11:]}')
print('-' * 50)

# ③ ‘홍길동’에서 이름만 출력하세요.
name = '홍길동'
print(f'이름: {name[1:]}')
print('-' * 50)

# ④ AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr에서 대문자, 소문자 따로 출력하세요.
str1 = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
print(f'대문자: {str1[::2]}')
print(f'소문자: {str1[1::2]}')
print('-' * 50)

# ⑤ ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ에서 숫자만 출력하세요.
str2 = 'ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ'
print(f'숫자: {str2[3::4]}')
print('-' * 50)

# ⑥ 주민등록번호는 881120-1068234입니다.
#    주민등록번호를 생년월일 부분과 숫자부분으로 나누어 출력하세요.
rNumber = '881120-1068234'
print(f'생년월일: {rNumber[:6]}')
print(f'숫자부분: {rNumber[7:]}')
print('-' * 50)

"""
2. 아래 조건에 만족하도록 코드 작성하세요.
"""
num1 = int(input("정수 입력: "))
print(f'10진수 : {num1}')
print(f'16진수 : {hex(num1)}')
print(f' 8진수 : {oct(num1)}')
print(f' 2진수 : {bin(num1)}')
print('-' * 50)

"""
3. 아래 조건에 만족하도록 코드 작성하세요.
"""
word1 = input("첫 번째 단어를 입력하세요: ")
word2 = input("두 번째 단어를 입력하세요: ")
word3 = input("세 번째 단어를 입력하세요: ")
print(f'코드 값이 가장   큰 단어 : {max(word1, word2, word3)}')
print(f'코드 값이 가장 작은 단어 : {min(word1, word2, word3)}')
print('-' * 50)

"""
4. 아래 조건에 만족하도록 코드 작성하세요.
"""
msg = "오늘은 행복한 목요일입니다."
input_msg = input("단어 입력: ")
print(f"'{input_msg}' 단어 메세지 존재 여부: {input_msg in msg}")
print('-' * 50)

"""
5. 아래 조건에 만족하도록 코드 작성하세요.
"""
input_word = input("단어 입력: ")
print(f"'{input_word}' 코드값 : {bin(ord(input_word[0]))} {bin(ord(input_word[1]))[2:]} {bin(ord(input_word[2]))[2:]}")
