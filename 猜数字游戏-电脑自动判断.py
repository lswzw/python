import random

secret = random.randint(1, 10000)
print('测试数为：'+str(secret)+'\n')
guess = random.randint(1, 10000)
lat_guess = 1
max_guess = 10000
print('输入随机数:'+str(guess))
b = 1
while guess != secret:
    if guess > secret:
        b +=1
        print('随机数字大了！'+'\n')
        max_guess = guess - 1
        guess = random.randint(lat_guess,max_guess)
        print('输入随机数:'+str(guess))
    else:
        b +=1
        print('随机数字小了！'+'\n')
        lat_guess = guess + 1
        guess = random.randint(lat_guess,max_guess)
        print('输入随机数:'+str(guess))
print('恭喜，您猜对了！')
print('\n'+'电脑用了'+str(b)+'次猜对数字！')
input('点击回车退出！')

