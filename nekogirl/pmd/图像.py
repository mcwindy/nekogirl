import 光标


size = 光标.长宽()
if size[0] < 80 or size[1] < 25:
    raise '窗口太小了，猫猫放不下。至少要80*25'
图像 = [[' ' for _ in range(size[0])] for __ in range(size[1])]


def 初始化边框():
    for i in range(1, size[1] - 1):
        for j in range(-1, 1):
            图像[i][j] = '║'
    for i in range(-1, 1):
        for j in range(1, size[0] - 1):
            图像[i][j] = '═'
    图像[0][0] = '╔'
    图像[0][-1] = '╗'
    图像[-1][0] = '╚'
    图像[-1][-1] = '╝'


def 显示(图像):
    for i in 图像:
        for j in i:
            print(j, end='')
        print()


def 绘制属性条():
    pass


if __name__ == '__main__':
    while True:
        初始化边框()
        显示(图像)
        p = 光标.位置()
        光标.去(p[0] + 3, p[1] - 5)
        inp = input()
