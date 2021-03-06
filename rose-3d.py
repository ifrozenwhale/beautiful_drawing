import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.pyplot as plt
import numpy as np

dx, dy = 0.215, 0.17
# dx, dy = 0.2, 0.17
# dx, dy = 0.087, 0.081


def in_love(x, y):
    # print(((x*0.5)**2+(y*1) ** 2-1)**3-(x*0.5)**2*(y*1)**3 <= 0)
    return (((x*dx)**2+(y*dy) ** 2-1)**3-(x*dx)**2*(y*dy)**3 <= 0)


cnt = 0


def draw_rose(fig, ax, i=0, j=0):
    if not in_love(i, j):
        return
    global cnt
    cnt += 1
    [x, t] = np.meshgrid(np.array(range(25)) / 24.0,
                         np.arange(0, 575.5, 500) / 575 * 17 * np.pi - 2 * np.pi)
    p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
    u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
    y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p))
    h = u * (x * np.cos(p) - y * np.sin(p))
    surf = ax.plot_surface(i+r * np.cos(t), j+r * np.sin(t), h,
                           cmap=cm.gist_heat, linewidth=0, antialiased=True)
    plt.pause(0.0001)


def scale_img(ax, x_scale=1, y_scale=1, z_scale=1):

    scale = np.diag([x_scale, y_scale, z_scale, 1.0])
    scale = scale*(1.0/scale.max())
    scale[3, 3] = 1.0

    def short_proj():
        return np.dot(Axes3D.get_proj(ax), scale)

    ax.get_proj = short_proj


def update_points(num):
    '''
    更新数据点
    '''
    point_ani.set_data(x[num], y[num])
    return point_ani,


fig = plt.figure(figsize=(15, 10))
ax = fig.gca(projection='3d')
maxv = 8
plt.axis('off')
ax.view_init(30, -85)
plt.tight_layout()
plt.ion()  # interactive mode on
for i in range(-maxv, maxv):
    for j in range(-maxv, maxv):
        if i == -maxv:
            scale_img(ax, i+4, 2, 1)
        else:
            scale_img(ax, i+4, maxv+3, 1)
        draw_rose(fig, ax, i, j)

# ax.text(6, 6, 0.5, s="521 Roses from Aoao", fontsize=10)
# ax.view_init()
plt.pause(3)

plt.savefig("./img/rose_test.pdf")
plt.show()
