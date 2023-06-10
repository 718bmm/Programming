import random

def find_num(x, guess):
    if 0 < guess < 11:
        if guess == x:
            print('Вы гений')
            return True
    else:
        print('enter number in range 1-10')
        return False
    

x = random.randint(1, 10)
while True:
    guess = int(input('find a secret number in range of 1-10: '))
    if 0 < guess < 11:
        if guess == x:
            print('Вы гений')
            break
    else:
        print('enter number in range 1-10')