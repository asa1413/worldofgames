from random import randint
from forex_python.converter import CurrencyRates


def get_money_interval(difficult):
    try:
        # get Currency Rate
        c = CurrencyRates()
        currency_rate = c.get_rate('USD', 'ILS')
        # get random number between 1-100
        random_number = randint(1,100)
        total_amount = random_number* currency_rate
        interval = 5-int(difficult)

        dict = {
            "currency_rate": currency_rate,
            "random_number": random_number,
            "total_amount": total_amount,
            "interval":interval
        }
        return(dict)
    except:
        print("error in CRM get_money_interval")

def get_guess_from_user(random_number):
    try:
        user_guess = -1
        while user_guess<1:
            user_guess = int(input("how many NIS is " + str(random_number) + " $:"))
            if user_guess<1:
                print("number must be positive")
        return (user_guess)
    except ValueError:
        print(" you must insert number")
        return 0
    except:
        print("error in get_guess_from_user")

def crgpaly(difficult):
    try:
        user_guess = 0
        dict = get_money_interval(difficult)
        #for x in dict.values():
         #   print(x)
        while user_guess ==0:
            user_guess = get_guess_from_user(dict.get("random_number"))
        # check user guess
        computer_sum = int(dict.get("total_amount"))
        interval = int(dict.get("interval"))
        if int(computer_sum) - int(interval) <= int(user_guess) <= int(computer_sum) + int(interval):
           # print("Great job , you won")
            return 1
        else:
            #print("You lost , try again")
            return 0

    except:
        print("error in crgpaly")

