import random
import time
import os

def generate_sequence(difficulty):
    try:
        list=[]
        for x in range(int(difficulty)):
            list.append(random.randint(1,101))
        return(list)
    except:
        print("error in MG generate_sequence")

def get_list_from_user(difficulty):
    try:
        user_list=[]
        for x in range(int(difficulty)):

            user_list.append(int(input("please enter number :")))
#        user_list = input("please enter the number split by ,")
        return(user_list)
    except ValueError:
        print("you can not insert string only integer, insert the numbers again")
        user_list.clear()
        return(user_list)
    except:
        print("error in MG get_list_from_user")

def is_list_equal(computer_list,user_list):
    try:
        status = bool(set(computer_list).intersection(user_list))
        return (status)
    except:
        print("error in MG is_list_equal")

def mgplay(difficulty):
    try:
        user_list=[]
        #get sequance of numbers
        computer_list = generate_sequence(difficulty)
        # print the list for 0.7 seconds
        for y in computer_list:
           print(y," , ", end= '')
        time.sleep(0.7)
        print("\n" * 100)
        #os.system('ilc') need to check why it doesn't work ##########
        while len(user_list) == 0:
            user_list = get_list_from_user(difficulty)
        # compre the lists
        status = is_list_equal(computer_list,user_list)
        if status:
        #    print("Great job , you won")
            return 1
        else:
         #   print("You lost , try again")
            return 0
    except:
        print("error in mgplay")
