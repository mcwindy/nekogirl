#!/usr/bin/env python

class Nekogirl():
    def __init__(self, name):
        self.name = name

    def 名字(self):
        return self.name

    def 喵喵喵(self):
        import random
        if random.random() < 0.5:  # 现在猫娘有概率不理你
            print('喵喵喵')

    def 变(self):
        print('变好了')

    def 自拍(self):
        print('''
                   \\
        |\__/,|   (`\\
      _.|o o  |_   ) )
    -(((---(((--------♥ ''')


if __name__ == '__main__':
    my_nekogirl = Nekogirl('sweety')
