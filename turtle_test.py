def print_hangman():
    import turtle as t
    x, y = 0, 100

    # t.shape('turtle')
    t.ht()
    t.penup()
    t.goto(x, y)
    # t.write(t.pos())
    t.pendown()
    t.goto(x + 0, y + 50)
    # t.write(t.pos())
    t.goto(x + -100, y + 50)
    # t.write(t.pos())
    t.goto(x + -100, y + -300)
    # t.write(t.pos())
    t.goto(x + -143.3, y + -325)
    # t.write(t.pos())
    t.goto(x + -100, y + -300)
    t.goto(x + -56.7, y + -325)
    # t.write(t.pos())
    yield None

    # 머리
    t.penup()
    t.goto(x + 0, y + -60)
    t.pendown()
    t.circle(30)
    # t.write(t.pos())
    yield None

    # 몸
    t.goto(x + 0, y + -150)
    # t.write(t.pos())
    t.penup()
    t.goto(x + 0, y + -60)
    t.pendown()
    yield None

    # 왼팔
    t.goto(x + -32.14, y + -98.3)
    # t.write(t.pos())
    t.goto(x + 0, y + -60)
    yield None

    # 오른팔
    t.goto(x + 32.14, y + -98.3)
    # t.write(t.pos())
    t.goto(x + 0, y + -60)
    yield None

    # 왼다리
    t.goto(x + 0, y + -150)
    t.goto(x + -25, y + -193)
    # t.write(t.pos())
    t.goto(x + 0, y + -150)
    yield None

    # 오른다리
    t.goto(x + 25, y + -193)
    # t.write(t.pos())
    yield None


def main():
    for i in range(6):
        print_hangman()
        input()


if __name__ == '__main__':
    main()
