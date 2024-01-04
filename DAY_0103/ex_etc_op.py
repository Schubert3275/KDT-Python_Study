# 바다코끼리연산자 => :=

msg = "Good!!"
n = len(msg)

if n <= 8:
    print(f"{n} : 정확한 데이터")
else:
    print(f"{n} : 8자 이하 입력 필수!")

msg = "Good!!"

if n := len(msg) <= 8:
    print(f"{n} : 정확한 데이터")
else:
    print(f"{n} : 8자 이하 입력 필수!")

print(s := "ABC")

# 2번 코드 -> := 사용
# s에 문자열을 할당하고, 'walrus' in s를 result에 할당하고, result가 True 라면
if result := 'walrus' in (s := 'walrus eat kimchi'):
    print(s)  # s 출력
    print(result)  # result 출력
