def in_love(x, y):
    return ((x*0.05)**2+(y*0.1) ** 2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0


l2 = []
#  将纵向每个字符当作 y 坐标的刻度
for y in range(15, -15, -1):
    l3 = []
    #  将横向每个字符当作 x 坐标的刻度
    for x in range(-30, 30):
        # 如果 x,y 点在心形内,则将一个字符加入到行,否则加入空字符
        l3.append(('U'if in_love(x, y) else' '))
    l2.append(''.join(l3))
l1 = '\n'.join(l2)
print(l1)
