from Live import load_game, welcome,choose_level
from GuessGame import ggplay
from MemoryGame import mgplay
from CurrencyRouletteGame import crgpaly
from Utils import Screen_cleaner
from Score import add_score

p_continue = 'y'
user_name = "asa" #input('insert your name:')

while p_continue == 'y':
    Screen_cleaner()
    print(welcome(user_name))
    #get game number and level
    game_number = load_game()
    game_difficulty = choose_level()


    if int(game_number)==1:
        status = ggplay(game_difficulty)
    elif int(game_number)==2:
        status = mgplay(game_difficulty)
    elif int(game_number)==3:
        status = crgpaly(game_difficulty)

    #print result and add score
    if status:
        add_score(game_difficulty,user_name)
        print("Great job , you won")
    else:
        print("You lost , try again")

    p_continue = input("do you want to play again y or n ?")