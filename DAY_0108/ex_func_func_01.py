def print_hello():
    hello = "hello~!"

    def print_message():
        msg = hello + " ^^ "
        print(msg)

    print_message()


def ff():
    x = 100

    def a():
        x = 10  # 함수 a의 지역변수 x

        def b():
            nonlocal x  # 가장 가까운 바깥 함수에서 변수 x를 찾음
            x = 20  # 함수 b의 지역변수 x
        b()
        print(x)
    a()


ff()
