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

# 머리
t.penup()
t.goto(x + 0, y + -60)
t.pendown()
t.circle(30)
# t.write(t.pos())

# 몸
t.goto(x + 0, y + -150)
# t.write(t.pos())
t.penup()
t.goto(x + 0, y + -60)
t.pendown()

# 왼팔
t.goto(x + -32.14, y + -98.3)
# t.write(t.pos())
t.goto(x + 0, y + -60)

# 오른팔
t.goto(x + 32.14, y + -98.3)
# t.write(t.pos())
t.goto(x + 0, y + -60)

# 왼다리
t.goto(x + 0, y + -150)
t.goto(x + -25, y + -193)
# t.write(t.pos())
t.goto(x + 0, y + -150)

# 오른다리
t.goto(x + 25, y + -193)
# t.write(t.pos())

input()
