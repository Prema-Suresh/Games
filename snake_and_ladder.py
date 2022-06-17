import random
  
snake = {17:8, 29:10, 36:2, 50:47, 59:21, 73:53, 78:65, 90:13, 95:66,97:84}
ladder = {3:22, 15:27, 18:24, 25:35, 34:48, 42:60, 44:63, 51:72, 54:68, 64:76, 67:75, 77:96, 80:99, 88:92}

position_1 = 0
position_2 = 0

def move(position):
    dice = random.randint(1,6)
    print(f'Dice : {dice}')
    position = position + dice
    if position in snake:
        print('Dang! bitten by a snake')
        position = snake[position]
        print(f'position : {position}')
    elif position in ladder:
        print('Woohoo! climbed the ladder')
        position = ladder[position]
        print(f'position : {position}')
    else:
             print(f'position : {position}')
    print('\n')
    return position

while True:
    A = input("Player 1, Press \"Enter\" to throw the dice:" )
    position_1 = move(position_1)
    if position_1 >= 100:
        print("Game Over!!!\nCongratulaions, Player 1 Wins\nThankyou for playing the game.")
        break
    B = input("Player 2, Press \"Enter\" to throw the dice:" )
    position_2 = move(position_2)
    if position_2 >= 100:
        print("Game Over!!!\nCongratulations, Player 2 Wins\nThankyou for playing the game.")
        break
