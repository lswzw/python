import random

secret = random.randint(1, 100)
guess = 0
i = 0
while guess != secret:
    try:
        guess = int(input('\n'+'请输入1-100的数字：'))
        if guess > secret:
            i += 1
            print('您输入的数字大了！')
        elif guess == secret:
            i += 1
            print('恭喜，您用'+str(i)+'次猜对了！')
        else:
            i += 1
            print('您输入的数字小了！！！')
    except:
        print('仅能输入数字！！！')
input('\n'+'点击回车退出！')

