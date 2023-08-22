# your code goes here!
import time

def countdown(int_arg):
    while int_arg >= 1:
        print(f'{int_arg} SECOND(S)!')
        int_arg -= 1
        if int_arg == 0:
            print("HAPPY NEW YEAR!")

def countdown_with_sleep(int):
    while int >= 1:
        print(f'{int} SECOND(S)!')
        time.sleep(1)
        int -= 1
        if int == 0:
            print("HAPPY NEW YEAR!")
