

# welcome def is used to greet the user
def welcome(name):
    try:
        return(print("Hello " + name + " and welcome to World Of Games." ,"\n" \
              "Here you can find many coll games to play."))
    except:
        print("opps problem with welcome def")

# in load game def the user choose the game
def load_game():
    try:
        game_description = "Please choose game to play:\n" \
                           "1.Guess Game - guess a number and see if you chose like computer\n" \
                           "2.Memory Game - a sequence of numbers will aooer for 1 second and you have" \
                           "to guss it back\n" \
                            "3.Currency Roulette - try and guess the value of a random amount of USD in ILS\n"

        game_to_play = input(game_description)

        l_statuss = number_in_range(game_to_play, 3, 1, "game")
        if l_statuss==1:
            load_game()
        else: return(game_to_play)
    except:
        print("problem in game_description section")

# in choose level def the user choose the difficulty
def choose_level():
    try:
        game_difficulty ="Please choose game difficulty from 1 to 5:"
        difficulty_to_play = input(game_difficulty)

        l_status =number_in_range(difficulty_to_play,5,1,"difficulty")
        if l_status ==1:
            choose_level()
        else: return(difficulty_to_play)
    except:
        print("problem in game_difficulty section")

# find if the number is in the right range
def number_in_range(user_val,max_val,min_val,name):
    try:
        if int(user_val) > max_val or int(user_val)<min_val:
            print("you inserted wrong value , please insert new value! \n")
            return 1
        else:
            return 0
    except:
        print("you inserted illegal "+ name +" value , please insert new value! \n")
        return 1
