import random
while True:
    random.seed(int(input('Enter seed: ')))

    random_side = random.randint(0, 1)

    if random_side == 0:
        print('Heads')

    else:
        print('Tails')
