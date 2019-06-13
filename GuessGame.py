import random

def generate_number(difficulty):
    try:
        return random.randint(1,int(difficulty))
    except:
        print("error in GG generate_number")

def get_guess_from_user(update_difficulty):
    try:
        x =0
        while (int(x) < 1) or (int(x)> int(update_difficulty)):
            temp = "please choose a number between 1 to "+ str(update_difficulty)
            x = int(input(temp))
        return x
    except ValueError:
        print("please insert number")
        return -1
    except:
        print("error in GG get_guess_from_user")

def compre_results(machine_generate_number,user_guess):
    try:
        if int(machine_generate_number) == int(user_guess):
            return 0 #true
        else:
            return 1 #false

    except:
        print("error in GG compre_results")

def ggplay(difficulty):
    try:
        user_guess = -1
        #update the difficulty range
        update_difficulty= 2* int(difficulty)
        #get random number
        machine_generate_number= generate_number(update_difficulty)
        # get guess from user
        while user_guess == -1:
            user_guess = get_guess_from_user(update_difficulty)
        user_machine_guess_result= compre_results(machine_generate_number,user_guess)
        # print result
        if user_machine_guess_result == 0:
          #  print("Great job , you won")
            return 1
        else:
           # print("You lost , try again")
            return 0
    except:
        print("error in ggplay methods")


