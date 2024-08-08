from random import randint

# Generate a random integer between 1 and 10 (inclusive)

print("Lets play Rock, Paper, Scissor.\n \nYou have to choose a number")
print("1 AS Scissor")
print('2 AS Paper')
print('3 AS Rock') 

Home = 0
AI_away = 0

rounds = int(input('Select number of rounds: '))

for i in range(rounds):
    #Select input
    play = int(input('Select a number from 1 to 3: '))

    #validating input
    while play < 1 or play > 3 :
        print('Please Select in the range number between 1 to 3')
        play = int(input('Select a number from 1 to 3: '))

    #generate random number between 1 and 3 & assigning with specific value
    random_number = randint(1, 3)

    # or might use this  to map the choices : 
    choices ={1: 'Scissor', 2: 'Paper', 3: 'Rock'}

    #Display computer choice
    print(f'\nMe: {choices[play]}', end='\n VS \n')
    print(f'Computer: {choices[random_number]}')

    # Scoring
    if random_number == play:
        print('Tie!')
    elif (play == 1 and random_number ==2) or (play == 2 and random_number == 3) or (play == 3 and random_number == 1):
        print('You Win!')
        Home += 1
    else:
        AI_away += 1
        print('You Lose!') 

#Decision         
if Home > AI_away:
    print('\nYou Win the Game!')
elif Home < AI_away:
    print('\nYou Lose the Game!')
else:
    print('\nTie the Game please try again')