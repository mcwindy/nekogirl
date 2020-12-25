import os
import ctypes

此处 = os.path.dirname(os.path.abspath(__file__))
a = ctypes.WinDLL(os.path.join(此处, 'cursor.dll'))
a.init()


def 去顶():
    a.gotoH()


def 去(x, y):
    a.gotoXY(x, y)


def 位置():
    t = a.getXY()
    return t // 65536, t % 65536


def 长宽():
    t = a.getWindowSize()
    # -1让光标在最后一行，不会让第一行出框
    print(t // 65536 - 1, t % 65536 - 1)
    return t // 65536 - 1, t % 65536 - 1


if __name__ == '__main__':
    for i in range(4):
        print(i)
    a.gotoH()
    print('nekogirl')
    print(长宽())
