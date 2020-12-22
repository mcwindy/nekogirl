class Nekogirl:
    states = {'猫猫', '猫娘'}

    def __init__(self, name, state='猫猫'):
        self.name = name
        self.state = state

    def 名字(self):
        return self.name

    def 叫(self):
        import random
        if self.state == '猫猫':
            if random.random() < 0.5:  # 现在猫猫有概率不理你
                print('喵喵喵')
        else:
            import time
            hour = int(time.asctime().split(' ')[3].split(':')[0])
            if hour < 8 or hour >= 18:
                cur = '晚上'
            elif 8 <= hour < 12:
                cur = '上午'
            else:
                cur = '下午'
            print('主人,' + cur + '好')

    def 变(self):
        self.state = str(*Nekogirl.states - {self.state})
        print('变好了')

    def 自拍(self):
        if self.state == '猫猫':
            print('''

          |\__/,|   (`
        _.|o o  |_   ) )
        -(((---(((--------♥ ''')
        else:
            print('还没有搞好TuT,可以发issue提供字符画或者照片')


if __name__ == '__main__':
    my_nekogirl = Nekogirl('sweety')
    my_nekogirl.名字()
    my_nekogirl.叫()
    my_nekogirl.自拍()
    my_nekogirl.变()
    my_nekogirl.叫()
    my_nekogirl.自拍()
