import random

def text(d):
    secret = random.randint(1, d)
    guess = random.randint(1, d)
    lat_guess = 1
    max_guess = d
    a = 1
    while guess != secret:
        if guess > secret:
            a += 1
            max_guess = guess - 1
            guess = random.randint(lat_guess, max_guess)
        else:
            a += 1
            lat_guess = guess + 1
            guess = random.randint(lat_guess, max_guess)
    return(a)

if __name__ == '__main__':
    b = 0
    d = int(input('输入猜测的最大数：'))
    for i in range(100):
        b += text(d)
    print('平均用'+str(b//100)+'次！')
    input('点击回车退出！')

