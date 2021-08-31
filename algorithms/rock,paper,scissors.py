from random import randint

choice = ['rock', 'paper', 'scissors']
computer = choice[randint(0, 2)]
player = input('Input your choice ').lower()
print(f'Computer choice : {computer}')

if player == computer:
    print('Draw')
elif player == 'rock' and computer == 'paper':
    print(f'Computer wins')
elif player == 'rock' and computer == 'scissors':
    print(f'You win')
elif player == 'paper' and computer == 'rock':
    print(f'You win')
elif player == 'paper' and computer == 'scissors':
    print(f'Computer wins')
elif player == 'scissors' and computer == 'rock':
    print(f'Computer wins')
elif player == 'scissors' and computer == 'paper':
    print(f'You win')
else:
    print(f'You chose wrong')
