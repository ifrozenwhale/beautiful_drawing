import turtle

# 设置初始位置
turtle.penup()  # 提起画笔
turtle.speed(100)
turtle.pensize(5)
turtle.left(90)  # 逆时针旋转九十度
turtle.fd(200)  # 向前移动一段距离 fd=forward
turtle.pendown()  # 放下画笔移动画笔开始绘制
turtle.right(90)   # 顺时针旋转九十度

# 花蕊
turtle.fillcolor("red")  # 填充颜色
turtle.begin_fill()  # 开始填充
turtle.circle(10, 180)  # 画一圆，10是半径，180是弧度
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30, 110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90, 70)
turtle.circle(30, 150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80, 90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150, 80)
turtle.left(50)
turtle.circle(150, 90)
turtle.end_fill()  # 结束填充

# 花瓣1
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
# urtle.setheading(angle) 或 turtle.seth(angle):改变行进方向 angle:行进方向的绝对角度，可以为负值
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)

# 花瓣2
turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)

# 叶子1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()

turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)

# 叶子2
turtle.right(90)
turtle.right(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(80, 90)
turtle.left(90)
turtle.circle(80, 90)
turtle.end_fill()

turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200, 60)
turtle.write('by 木子欢儿', font=("Bradley Hand ITC", 30, "bold"))  # 文字可以自己修改
# 设置成画完不会自动退出
turtle.done()
